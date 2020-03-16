from django.contrib import admin

from mapping.admin import manager_admin, site_admin
from .models import (ChartStyle, Operation, OperationMethod, OperationType,
                     Part, Sheet,)


# @admin.register(ChartStyle)
# class ChartStyleAdmin(NestedModelAdmin):
#     model = ChartStyle
#     list_display = [
#         'background_color',
#         'is_striped']


# class ChartStyleInline(NestedTabularInline):
#     model = ChartStyle


@admin.register(OperationMethod, site=manager_admin)
class OperationMethodAdmin(admin.ModelAdmin):
    model = OperationMethod
    fields = ['name', 'description', 'use_work_period']
    list_display = [
        'name',
        'description',
        'use_work_period']
    list_filter = ['use_work_period',]

    def get_queryset(self, request):
        "Filter by Company"
        qs = super(OperationMethodAdmin, self).get_queryset(request)
        return qs.filter(company=request.user.company)


@admin.register(OperationType, site=site_admin)
class SiteOperationTypeAdmin(admin.ModelAdmin):
    model = OperationType
    # inlines = [ChartStyleInline]
    fields = [
        'name',
        'description',
        'value_type',]
    list_display = [
        'name',
        'description',
        'value_type',]
        # 'chart_style']
    list_filter = ['value_type']
    search_fields = ['name', 'value_type']


class PartSheetInline(admin.TabularInline):
    model = Sheet
    exclude = ['description']
    readonly_fields = [
        'creator',
        'release_date',
        'raw_materials_estimate',
        'logistics_estimate',
        'office_estimate',
        'finished_goods_estimate']
    extra = 0

    def get_queryset(self, request):
        return Sheet.objects.all()

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Part, site=manager_admin)
class PartAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'creator', 'date_updated']
    list_filter = ['date_created', 'date_updated']
    search_fields = ['name']
    inlines = [PartSheetInline]
    readonly_fields = ('creator',)

    def get_queryset(self, request):
        "Filter by Company"
        qs = super(PartAdmin, self).get_queryset(request)
        return qs.filter(creator__company=request.user.company)
