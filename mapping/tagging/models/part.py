from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.db import models

from mapping.common.middleware import get_current_user
from mapping.common.mixins import TimestampsMixin


@python_2_unicode_compatible
class Part(TimestampsMixin):
    "Parts being tracked."
    name = models.CharField(
        'part name',
        help_text='Part name',
        max_length=150,)

    description = models.TextField(
        'part description',
        help_text='Part description',
        null=True,)

    # Part company is inferred by ownership
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        help_text='Part creator',
        related_name='parts',)

    def save(self, *args, **kwargs):
        "Assign the current user as the creator."
        if self.pk is None:
            self.creator = get_current_user()
        super(Part, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
