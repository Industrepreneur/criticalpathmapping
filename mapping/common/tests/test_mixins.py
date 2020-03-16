# import pytest

from mapping.common.mixins import TimestampsMixin


class TestModelStub(TimestampsMixin):
    """Test Model, inherits TimestampsMixin"""


class TestTimestampsMixin:

    def test_timestamps_mixin_is_abstract(self):
        """
        Mixins are not meant to be used directly.
        """
        assert hasattr(TimestampsMixin.Meta, 'abstract')

    def test_timestamps_mixin_adds_date_created_field(self):
        """
        TimestampsMixin should add a date_created DateTimeField, set to the
        current time when a record is created.
        """
        assert hasattr(TestModelStub(), 'date_created')

    def test_timestamps_mixin_adds_date_updated_field(self):
        """
        TimestampsMixin should add a date_updated DateTimeField, set to the
        current time when a record is created.
        """
        assert hasattr(TestModelStub(), 'date_updated')

    def test_timestamps_mixin_date_updated_field_updates_on_save(self):
        """
        date_updated field added by TimestampsMixin should be updated to the
        current time when a record is modified.
        """
