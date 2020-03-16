from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from mapping.common.mixins import TimestampsMixin


@python_2_unicode_compatible
class WorkShift(TimestampsMixin):
    "Working Period Shift"

    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6

    DAY_OF_WEEK_CHOICES = (
        (SUNDAY, 'Sunday'),
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'))

    day_of_week = models.PositiveSmallIntegerField(
        'day of week',
        help_text='Day of week shift starts on.',
        choices=DAY_OF_WEEK_CHOICES,
        default=MONDAY,)

    time_shift_starts = models.TimeField(
        'shift start time',
        help_text='Shift start',)

    time_shift_ends = models.TimeField(
        'shift end time',
        help_text='Shift end',)

    work_period = models.ForeignKey(
        'WorkPeriod',
        related_name='work_shifts',)

    class Meta:
        db_table = 'accounts_work_shift'
        ordering = ['day_of_week', 'time_shift_starts']

    def __str__(self):
        return "%s from: %s until: %s" % (
            self.DAY_OF_WEEK_CHOICES[self.day_of_week][1],
            self.time_shift_starts,
            self.time_shift_ends,)
