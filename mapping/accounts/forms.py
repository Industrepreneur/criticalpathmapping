import datetime
from django import forms
from django.utils import timezone

from .models import Company, User
# from .models import User


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    company = forms.CharField(max_length=30, label='Company')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_manager = True

        # current_tz = timezone.get_current_timezone()
        expiration = datetime.datetime.now() + datetime.timedelta(days=90)
        # user.expiration = current_tz.normalize(expiration)
        user.expiration = timezone.make_aware(expiration)

        # Register a company first
        company = Company(name=self.cleaned_data['company'])
        company.is_active = True
        company.user_limit = 5
        company.save()

        user.company = company
        user.save()
