from rest_framework.mixins import (CreateModelMixin,
                                   DestroyModelMixin,
                                   RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.viewsets import GenericViewSet


class CreateRetrieveDeleteViewSet(CreateModelMixin,
                                  DestroyModelMixin,
                                  RetrieveModelMixin,
                                  UpdateModelMixin,
                                  GenericViewSet):
    pass
