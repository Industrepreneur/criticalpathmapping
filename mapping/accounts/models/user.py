from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone
import datetime

from mapping.common.mixins import TimestampsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        "Create and saves a user with provided credentials."
        if not email:
            raise ValueError('Users must have a valid email address.')

        now = timezone.now()
        user = self.model(
            email=self.normalize_email(email.lower()),
            is_active=True,
            is_manager=False,
            is_admin=False,
            last_login=now,
            **extra_fields)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and saves a superuser with the provided credentials.
        """
        user = self.create_user(email, password, **extra_fields)
        user.is_manager = True
        user.is_admin = True
        user.save()
        return user


@python_2_unicode_compatible
class User(AbstractBaseUser, TimestampsMixin):
    """
    Custom User class for Factory Concepts.

    Derived from standard Django auth system. Replaces username with email
    as the primary identifier.

    Email and password are required.  All other fields are optional.
    """
    email = models.EmailField(
        'email address',
        help_text='Full email address, which acts as a primary, '
                  'unique identifier.',
        max_length=255,
        unique=True,)

    first_name = models.CharField(
        'first name',
        help_text='Account holders first name.',
        max_length=30,
        blank=False,)

    last_name = models.CharField(
        'last name',
        help_text='Account holders last name.',
        max_length=30,
        blank=False,)

    expiration = models.DateTimeField(
        'expiration date',
        help_text='Account expiration date.',
        blank=True,
        null=True,)

    is_active = models.BooleanField(
        'active',
        default=True,
        help_text='Whether this user should be treated as active. '
                  'Unselect this instead of deleting accounts.',)

    is_manager = models.BooleanField(
        'manager',
        default=False,
        help_text='Whether the user can manage users and other '
                  'company-specific functionality.',)

    is_admin = models.BooleanField(
        'admin',
        default=False,
        help_text='Whether the user can manage all companies, users, and operation types.',)

    company = models.ForeignKey(
        'Company',
        help_text='Company this user belongs to',
        null=True,
        related_name='users',)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        """
        Returns first name, last name, and email in the form of:
        {first} {last} <email>
        """
        return self.email

    def get_full_name(self):
        "Returns the users' first name and last name separated by a space."
        return ' '.join([self.first_name, self.last_name]).strip()
    get_full_name.short_description = 'Full Name'

    def get_short_name(self):
        "Returns the first name."
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def full_name(self):
        "Returns the users' full name"
        return self.get_full_name()

    @property
    def is_staff(self):
        "Is this user a group administrator"
        return self.is_manager
