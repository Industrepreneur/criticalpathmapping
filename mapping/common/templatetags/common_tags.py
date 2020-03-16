import os
from django import template


register = template.Library()


@register.simple_tag
def app_version():
    "Retrieve the current Application version from environment."
    return os.environ.get('APP_VER', '').replace('_', ' ')
