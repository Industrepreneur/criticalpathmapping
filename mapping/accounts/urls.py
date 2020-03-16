from rest_framework_extensions.routers import ExtendedSimpleRouter

from .views import WorkPeriodViewSet, WorkShiftViewSet


router = ExtendedSimpleRouter(trailing_slash=False)

(router.register(r'work_periods', WorkPeriodViewSet, base_name='workperiod')
       .register(r'work_shifts',
                 WorkShiftViewSet,
                 base_name='workperiods-shift',
                 parents_query_lookups=['work_period']))

urlpatterns = router.urls
