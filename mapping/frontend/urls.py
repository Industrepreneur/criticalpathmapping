from django.conf.urls import url

from .views import AppView


urlpatterns = [
    url('^.*$', AppView.as_view(), name='app'),
]
