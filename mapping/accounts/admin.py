from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group

from mapping.admin import manager_admin, site_admin
from mapping.common.middleware import get_current_user
from .models import User, Company
from .models import WorkPeriod, WorkShift

#####################
####### Manager Admin
#####################

class UserCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required fields,
    plus a repeated password.
    """
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,)
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = user.email.lower()
        # Assign the current users company
        user.company = get_current_user().company
        # Save the provided password in hashed form
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on the user,
    replacing the password field with admin's password hash display field.
    """
    password = ReadOnlyPasswordHashField(
        label='Password',
        help_text="Raw passwords are not stored, so there is no way to view "
                  "this user's password, but you can <a href=\"password/\">"
                  "change the password using this form</a>.",)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            # 'user_profile__company',
            'password',
            'is_active',
            'is_manager',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the field
        # does note have access to the initial value.
        return self.initial["password"]


@admin.register(User, site=manager_admin)
class UserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_manager',)
    list_filter = ('is_active', 'is_manager',)
    fieldsets = (
        (None, {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'password',)}
        ),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_manager',)}
        ),
    )
    # add_fieldsets is not a standard ModelAdmin attribute.
    # UserAdmin overrides get_fieldsets to use this attribute
    # when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2',)}),
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',)
    ordering = ('email',)
    filter_horizontal = ()

    def get_queryset(self, request):
        "Filter by Company"
        qs = super(UserAdmin, self).get_queryset(request)
        return qs.filter(company=request.user.company)


class WorkPeriodShiftInline(admin.TabularInline):
    model = WorkShift
    extra = 0

    def get_queryset(self, request):
        "Filter by Company"
        user = request.user
        return WorkShift.objects.filter(work_period__company=user.company)


@admin.register(WorkPeriod, site=manager_admin)
class WorkPeriodAdmin(admin.ModelAdmin):
    model = WorkPeriod
    fields = ['name', 'description']
    readonly_fields = ['company']
    list_display = ['name', 'description']
    inlines = [WorkPeriodShiftInline]

    def get_queryset(self, request):
        "Filter by Company"
        qs = super(WorkPeriodAdmin, self).get_queryset(request)
        return qs.filter(company=request.user.company)



##################
####### Site Admin
##################

class SiteUserCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required fields,
    plus a repeated password.
    """
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,)
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed form
        user = super(SiteUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class SiteUserChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on the user,
    replacing the password field with admin's password hash display field.
    """
    password = ReadOnlyPasswordHashField(
        label='Password',
        help_text="Raw passwords are not stored, so there is no way to view "
                  "this user's password, but you can <a href=\"password/\">"
                  "change the password using this form</a>.",)

    class Meta:

        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'is_active',
            'is_manager',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the field
        # does note have access to the initial value.
        return self.initial["password"]


class SiteUserInline(admin.TabularInline):
    model = User
    extra = 0
    exclude = ['email', 'password']
    readonly_fields = [
        'first_name',
        'last_name',
        'is_active',
        'is_manager',
        'is_admin',
        'last_login',]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Company, site=site_admin)
class SiteCompanyAdmin(admin.ModelAdmin):
    model = Company
    inlines = [SiteUserInline]
    list_display = ['name', 'is_active', 'user_limit']
    list_filter = ['is_active', 'date_created', 'date_updated']
    search_fields = ['name']
    fieldsets = [
        (None, {
            'fields': (
                ('name', 'is_active'),
                ('user_limit')
            )})
    ]


@admin.register(User, site=site_admin)
class SiteUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = SiteUserChangeForm
    add_form = SiteUserCreationForm
    list_display = (
        'email',
        'first_name',
        'last_name',
        'company',
        'date_created',
        'expiration',
        'is_active',
        'is_manager',
        'is_admin',)
    list_filter = ('is_active', 'is_manager', 'is_admin',)
    fieldsets = (
        (None, {
            'fields': (
                'first_name',
                'last_name',
                'company',
                'email',
                'password',
                'expiration',)}
        ),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_manager',
                'is_admin',)}
        ),
    )
    # add_fieldsets is not a standard ModelAdmin attribute.
    # UserAdmin overrides get_fieldsets to use this attribute
    # when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'company',
                'password1',
                'password2',)}),
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',
        'company__name'
    )
    ordering = ('email',)
    filter_horizontal = ()

    def get_queryset(self, request):
        # return User.objects.all()
        # "Filter by Company"
        return super(UserAdmin, self).get_queryset(request)
    #     # if request.user.is_superuser:
    #     #     return qs
    #     # return qs.filter(company=request.user.company)


admin.site.unregister(Group)
# admin.site.unregister(Permission)
