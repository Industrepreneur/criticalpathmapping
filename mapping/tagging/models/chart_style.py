from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from mapping.common.mixins import TimestampsMixin


@python_2_unicode_compatible
class ChartStyle(TimestampsMixin):
    "Chart style configuration."

    background_color = models.CharField(
        'background color',
        help_text='Color used to represent this item when rendering '
                  'in MAPs and Pie charts.  Examples: #8e44ad, '
                  'rgb(212, 48, 100), rgb(212, 48, 100, 0.8), '
                  'hsla(145, 78%, 68%), or hsla(145, 78%, 68%, 0.5)',
        max_length=50,)

    is_striped = models.BooleanField(
        'has stripes',
        help_text='Whether item is rendered with a stripe overlay '
                  'in MAPs and Pie charts.',
        default=False,)

    class Meta:
        db_table = 'tagging_chart_style'
        unique_together = (('background_color', 'is_striped'),)

    def __str__(self):
        return "{color} {striped}".format(
            color=self.background_color,
            striped=self.is_striped)
