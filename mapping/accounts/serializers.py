from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers

from .models import Company, User, WorkPeriod, WorkShift


class CompanySerializer(serializers.ModelSerializer):
    "Serializer for Companies"

    class Meta:
        model = Company
        fields = ('name', 'is_active', 'user_limit', 'date_created',
                  'date_updated')
        read_only_fields = ('date_created', 'date_updated')


class UserSerializer(serializers.ModelSerializer):
    "Serializer for Users"

    company = CompanySerializer(read_only=True, required=False)
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'full_name',
                  'company', 'date_created', 'date_updated', 'password',
                  'confirm_password')
        read_only_fields = ('first_name', 'company', 'date_created',
                            'date_updated')

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()

        # Update the current session to prevent forced re-login
        update_session_auth_hash(self.context.get('request'), instance)

        return instance


class WorkShiftSerializer(serializers.ModelSerializer):
    "Serializer for Work Period Shifts."

    class Meta:
        model = WorkShift
        fields = ('id', 'day_of_week', 'time_shift_starts', 'time_shift_ends',
                  'work_period', 'date_created', 'date_updated')
        read_only_fields = ('date_created', 'date_updated')


class WorkPeriodSerializer(serializers.ModelSerializer):
    "Serializer for Working Periods."
    work_shifts = WorkShiftSerializer(many=True, read_only=True, required=False)

    company = CompanySerializer(read_only=True, required=False)

    class Meta:
        model = WorkPeriod
        fields = ('id', 'name', 'description', 'company', 'work_shifts',
                  'date_created', 'date_updated')
        read_only_fields = ('company', 'date_created', 'date_updated')
