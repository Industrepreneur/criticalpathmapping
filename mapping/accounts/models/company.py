from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MinValueValidator
from django.db import models

from mapping.common.mixins import TimestampsMixin


@python_2_unicode_compatible
class Company(TimestampsMixin):
    "Company"
    name = models.CharField(
        'company name',
        max_length=150,)

    is_active = models.BooleanField(
        'active',
        help_text='Company status',
        default=False,)

    user_limit = models.PositiveSmallIntegerField(
        'user limit',
        help_text='Max. number of users allowed',
        default=10,
        validators=[MinValueValidator(1)],)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name
