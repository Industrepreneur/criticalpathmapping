from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from mapping.common.middleware import get_current_user
from mapping.common.mixins import TimestampsMixin


@python_2_unicode_compatible
class OperationMethod(TimestampsMixin):
    """
    Operation Methods

    Defined uniquely for each company, these are used to distinguish operations
    that are calculated using work periods, and those that are not.

    TODO: Each company should probably start with basic defaults.

    Examples:
      - Mill:3-Axis
      - Press Brake
      - Anodize
      - Heat Treat
      - Outside Processing
    """

    name = models.CharField(
        'name',
        help_text='The name of the operation (Mill:3-Axis, Heat Treat, '
                  'Anodize, Outside Processing, ...)',
        max_length=50,)

    description = models.TextField(
        'description',
        help_text='Optional description for the operation',
        blank=True,
        null=True,)

    use_work_period = models.BooleanField(
        'use work period',
        help_text='Determines whether this specific operation method is '
                  'calculated using work periods.',
        default=False,)

    company = models.ForeignKey(
        'accounts.Company',
        related_name='operation_methods',)

    class Meta:
        db_table = 'tagging_operation_method'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Assign the current users company."""
        # if self.pk is None and 'company' not in self:
        if self.pk is None:
            user = get_current_user()
            self.company = user.company
        super(OperationMethod, self).save(*args, **kwargs)
