"""
Settings overrides for staging server.

Rather than inheriting directly from base, this file derives its settings from
production, in order to prevent repetition while keeping environments inline.
"""
from .production import *
