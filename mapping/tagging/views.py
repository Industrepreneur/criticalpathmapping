from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from mapping.common.viewsets import CreateRetrieveDeleteViewSet
from .models import (ChartStyle, Part, Sheet, Operation, OperationMethod,
                     OperationType)
from .serializers import (ChartStyleSerializer, PartSerializer,
                          SheetSerializer, OperationSerializer,
                          OperationMethodSerializer, OperationTypeSerializer)


class ChartStyleViewSet(NestedViewSetMixin, ModelViewSet):
    "API endpoint for accessing Chart Styles."
    serializer_class = ChartStyleSerializer

    def get_queryset(self):
        return ChartStyle.objects \
                         .order_by('is_striped', 'background_color')


class PartViewSet(NestedViewSetMixin, ModelViewSet):
    "API endpoint that allows Parts to be viewed or edited."
    serializer_class = PartSerializer
    # permission_classes = [
    #     permissions.IsAuthenticated,
    #     # IsOwnerOrStaff,
    # ]

    def get_queryset(self):
        "Filter by Company"
        user = self.request.user
        return Part.objects \
                   .filter(creator__company=user.company) \
                   .order_by('-date_created')


class NestedSheetViewSet(NestedViewSetMixin, ModelViewSet):
    "API endpoint for Tagging Sheets when nested below Parts"
    serializer_class = SheetSerializer

    def get_queryset(self):
        "Filter by Company."
        user = self.request.user or None
        part_id = self.kwargs['parent_lookup_part'] or None
        return Sheet.objects \
                    .filter(creator__company=user.company,
                            part__id=part_id) \
                    .order_by('-date_created')


class SheetViewSet(NestedViewSetMixin, CreateRetrieveDeleteViewSet):
    "API endpoint for Tagging Sheets"
    serializer_class = SheetSerializer

    def get_queryset(self):
        "Filter by Company."
        user = self.request.user
        return Sheet.objects \
                    .filter(creator__company=user.company) \
                    .order_by('-date_created')


class NestedOperationViewSet(NestedViewSetMixin, ModelViewSet):
    "API endpoint for Tagging Sheet Operations."
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer

    def get_queryset(self):
        "Filter by Company"
        user = self.request.user
        sheet_id = self.kwargs['parent_lookup_sheet'] or None
        return Operation.objects \
                        .filter(sheet__creator__company=user.company,
                                sheet__id=sheet_id) \
                        .order_by('date_started')


# TODO: This should be a POST-only View rather than a full ViewSet
class OperationViewSet(NestedViewSetMixin, CreateRetrieveDeleteViewSet):
    "API endpoint for Tagging Sheet Operations."
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        "Filter by Company"
        user = self.request.user
        return Operation.objects \
                        .filter(sheet__creator__company=user.company) \
                        .order_by('date_started')


class OperationMethodViewSet(ModelViewSet):
    """
    API endpoint for Operation Methods

    This is read-only, for lookup use. Modifications should be made using the
    main admin interface.
    """
    queryset = OperationMethod.objects.all()
    serializer_class = OperationMethodSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        "Filter by Company."
        user = self.request.user
        return OperationMethod.objects \
                              .filter(company=user.company) \
                              .order_by('name')


class OperationTypeViewSet(ReadOnlyModelViewSet):
    """
    API endpoint for Operation Types

    This is read-only, for lookup use. Modifications should be made using the
    backend admin interface.
    """
    queryset = OperationType.objects \
                            .all() \
                            .order_by('name')
    serializer_class = OperationTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
