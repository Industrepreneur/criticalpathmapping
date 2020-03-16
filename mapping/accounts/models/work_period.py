from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from mapping.common.middleware import get_current_user
from mapping.common.mixins import TimestampsMixin


@python_2_unicode_compatible
class WorkPeriod(TimestampsMixin):
    "Working Period"
    name = models.CharField(
        'name',
        help_text='Work period name',
        max_length=150,)

    description = models.TextField(
        'description',
        help_text='Work period description',
        null=True,)

    is_default = models.BooleanField(
        'default period',
        help_text='Specifies whether this is the default Work Period.',
        default=False,)

    company = models.ForeignKey(
        'Company',
        help_text='Company this work period belongs to',
        related_name='work_periods',)

    class Meta:
        db_table = 'accounts_work_period'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        "Assign the current users company."
        if self.pk is None:
            user = get_current_user()
            self.company = user.company

        super(WorkPeriod, self).save(*args, **kwargs)
