from rest_framework.serializers import ModelSerializer

from .models import (ChartStyle, Operation, OperationMethod, OperationType,
                     Part, Sheet)


class ChartStyleSerializer(ModelSerializer):
    "Serializer for Chart Styles."

    class Meta:
        model = ChartStyle
        fields = ('id', 'background_color', 'is_striped')


class OperationMethodSerializer(ModelSerializer):
    "Serializer for Operation Methods."

    class Meta:
        model = OperationMethod
        fields = ('id', 'name', 'description', 'use_work_period',
                  'company', 'date_created', 'date_updated')
        read_only_fields = ('company', 'date_created', 'date_updated')


class OperationTypeSerializer(ModelSerializer):
    "Serializer for Operation Types."
    chart_style = ChartStyleSerializer(read_only=True, required=False)

    class Meta:
        model = OperationType
        fields = ('id', 'name', 'description', 'value_type',
                  'chart_style', 'date_created', 'date_updated')
        read_only_fields = ('chart_style', 'date_created', 'date_updated')


class OperationSerializer(ModelSerializer):
    "Serializer for Tagging Sheet Operations."

    class Meta:
        model = Operation
        fields = ('id', 'description', 'operation_method', 'operation_type',
                  'work_period', 'quantity_in', 'quantity_out', 'date_started',
                  'date_completed', 'value_type')
        read_only_fields = ('value_type',)

    def create(self, validated_data):
        # Inject sheet_id before saving
        sheet_id = self.initial_data['sheet']['id']
        validated_data['sheet'] = Sheet.objects.get(pk=sheet_id)
        return Operation.objects.create(**validated_data)


class PartSerializer(ModelSerializer):
    "Serializer for Company Parts."

    class Meta:
        model = Part
        fields = ('id', 'name', 'description', 'creator',
                  'date_created', 'date_updated')
        read_only_fields = ('creator', 'date_created', 'date_updated')


class SheetSerializer(ModelSerializer):
    "Serializer for Tagging Sheets."
    part = PartSerializer(read_only=True, required=False)
    operations = OperationSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Sheet
        fields = ('id', 'part', 'description', 'creator', 'operations',
                  'raw_materials_estimate', 'logistics_estimate',
                  'office_estimate', 'finished_goods_estimate',
                  'release_date', 'date_created', 'date_updated')
        read_only_fields = ('creator', 'date_created', 'date_updated')

    def create(self, validated_data):
        # Inject part_id before saving
        part_id = self.initial_data['part']['id']
        validated_data['part'] = Part.objects.get(pk=part_id)
        return Sheet.objects.create(**validated_data)
