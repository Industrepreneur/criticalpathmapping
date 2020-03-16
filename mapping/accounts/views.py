from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response

from .models import Company, User, WorkPeriod, WorkShift
from .permissions import IsAccountOwner
from .serializers import (CompanySerializer, UserSerializer,
                          WorkPeriodSerializer, WorkShiftSerializer)


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class UserViewSet(ModelViewSet):
    lookup_field = 'email'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            User.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data,
                            status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)

        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                serialized = UserSerializer(user)
                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Invalid Username/password combination.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)


class WorkPeriodViewSet(ReadOnlyModelViewSet):
    """
    API view for Work Periods

    This is read-only, for lookup use. Modifications should be made using the
    backend admin interface.
    """
    queryset = WorkPeriod.objects.all()
    serializer_class = WorkPeriodSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        "Filter by Company"
        user = self.request.user
        return WorkPeriod.objects \
                         .filter(company=user.company) \
                         .order_by('name')


class WorkShiftViewSet(ReadOnlyModelViewSet):
    """
    API view for Work Period Shifts

    This is read-only, for lookup use. Modifications should be made using the
    backend admin interface.
    """
    queryset = WorkShift.objects.all()
    serializer_class = WorkShiftSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        "Filter by Company and Work Period"
        user = self.request.user
        work_period_id = self.kwargs['parent_lookup_work_period'] or None
        return WorkShift.objects.filter(work_period__company=user.company,
                                        work_period__id=work_period_id) \
                                .order_by('day_of_week', 'time_shift_starts')
