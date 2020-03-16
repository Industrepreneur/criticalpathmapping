from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator


class AppView(TemplateView):
    template_name = 'app.html'

    # @method_decorator(ensure_csrf_cookie)
    def render_to_response(self, context, **response_kwargs):
        response = super(AppView, self).render_to_response(context, **response_kwargs)
        return response

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(AppView, self).dispatch(*args, **kwargs)
