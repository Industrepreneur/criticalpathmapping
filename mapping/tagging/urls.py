from rest_framework_extensions.routers import ExtendedSimpleRouter

from .views import (ChartStyleViewSet, PartViewSet, NestedSheetViewSet,
                    SheetViewSet, NestedOperationViewSet,
                    OperationMethodViewSet, OperationTypeViewSet,
                    OperationViewSet)


router = ExtendedSimpleRouter(trailing_slash=False)

router.register(r'chart_styles',
                ChartStyleViewSet,
                base_name='chartstyle')

router.register(r'operation_methods',
                OperationMethodViewSet,
                base_name='operationmethod')

router.register(r'operation_types',
                OperationTypeViewSet,
                base_name='operationtype')

router.register(r'operations',
                OperationViewSet,
                base_name='operation')

(router.register(r'parts', PartViewSet, base_name='part')
       .register(r'sheets',
                 NestedSheetViewSet,
                 'parts-sheet',
                 parents_query_lookups=['part']))

(router.register(r'sheets', SheetViewSet, base_name='sheet')
       .register(r'operations',
                 NestedOperationViewSet,
                 'sheets-operation',
                 parents_query_lookups=['sheet']))

urlpatterns = router.urls
