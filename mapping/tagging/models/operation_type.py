from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from mapping.common.mixins import TimestampsMixin


@python_2_unicode_compatible
class OperationType(TimestampsMixin):
    """
    Operation Types

    Global to all companies, these are used to determine the operation type

    Examples:
      - Processing, Piece
      - Processing, Batch
      - Inspection, Batch
      - Setup
      - Outside Processing
      - Wait For Resource


    Value Types
    -----------
    Global to all companies, these are used to categorize the value
    type of the specified operation.

    Examples:
      - Value Add (VA)
      - Non-Value Add (NVA)
      - Required Non-Value Add (RNVA)
    """

    VALUE_ADD = 'VA'
    NON_VALUE_ADD = 'NVA'
    REQ_NON_VALUE_ADD = 'RNVA'

    VALUE_TYPE_CHOICES = (
        (VALUE_ADD, 'Value Add'),
        (NON_VALUE_ADD, 'Non Value Add'),
        (REQ_NON_VALUE_ADD, 'Required, Non Value Add'),)

    name = models.CharField(
        'operation type',
        help_text='The type of operation',
        max_length=50,
        unique=True,)

    description = models.TextField(
        'description',
        help_text='Optional description for the operation type',
        blank=True,
        null=True,)

    value_type = models.CharField(
        'value type',
        help_text='Value type classification (Value Add, Non Value Add, '
                  'Required, Non Value Add)',
        max_length=4,
        choices=VALUE_TYPE_CHOICES,
        default=VALUE_ADD,)

    chart_style = models.ForeignKey(
        'ChartStyle',
        related_name='operation_type',
        null=True,)

    class Meta:
        db_table = 'tagging_operation_type'

    def __str__(self):
        return self.name
