from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.db import models

from mapping.common.middleware import get_current_user
from mapping.common.mixins import TimestampsMixin


@python_2_unicode_compatible
class Sheet(TimestampsMixin):
    "Tagging sheet."

    description = models.TextField(
        'sheet description',
        help_text='Sheet Description',
        null=True,)

    raw_materials_estimate = models.DecimalField(
        'raw materials estimate',
        help_text='Time estimate for raw materials (in days)',
        default=0,
        max_digits=5,
        decimal_places=2,)

    logistics_estimate = models.DecimalField(
        'logistics estimate',
        help_text='Time estimate for logistics (in days)',
        default=0,
        max_digits=5,
        decimal_places=2,)

    office_estimate = models.DecimalField(
        'office estimate',
        help_text='Time estimate for office tasks (in days)',
        default=0,
        max_digits=5,
        decimal_places=2,)

    finished_goods_estimate = models.DecimalField(
        'finished goods estimate',
        help_text='Time estimate for finished goods (in days)',
        default=0,
        max_digits=5,
        decimal_places=2,)

    release_date = models.DateTimeField(
        'release date',
        help_text='Sheet release date',
        null=True,)

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='sheets',)

    part = models.ForeignKey(
        'Part',
        related_name='sheets',)

    def save(self, *args, **kwargs):
        "Assign the current user as the creator."
        if self.pk is None:
            self.creator = get_current_user()
        super(Sheet, self).save(*args, **kwargs)

    def __str__(self):
        return self.description
