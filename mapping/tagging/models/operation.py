from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from mapping.common.mixins import TimestampsMixin


@python_2_unicode_compatible
class Operation(TimestampsMixin):
    "Operation entry for a specific Tagging Sheet"

    description = models.TextField(
        'operation description',
        help_text='Operation description',
        null=True,
        blank=True,)

    date_started = models.DateTimeField(
        'start date',
        help_text='Operation start date',
        null=True,)

    # TODO: Add validator for not null if operation started is set
    date_completed = models.DateTimeField(
        'end date',
        help_text='Operation end date',
        null=True,)

    quantity_in = models.PositiveIntegerField(
        'quantity in',
        help_text='The incoming quantity',
        null=True,)

    quantity_out = models.PositiveIntegerField(
        'quantity out',
        help_text='The outgoing quantity',
        null=True,)

    operation_method = models.ForeignKey(
        'OperationMethod',
        related_name='operations',)

    operation_type = models.ForeignKey(
        'OperationType',
        related_name='operations',)

    work_period = models.ForeignKey(
        'accounts.WorkPeriod',
        related_name='operations',)

    sheet = models.ForeignKey(
        'Sheet',
        related_name='operations',)

    @property
    def value_type(self):
        return self.operation_type.value_type

    class Meta:
        ordering = ['date_started']

    def __str__(self):
        return "%i" % self.pk
