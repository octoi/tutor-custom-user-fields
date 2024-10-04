from django.conf import settings

def plugin_settings(settings):
    settings.ADDL_INSTALLED_APPS = getattr(settings, 'ADDL_INSTALLED_APPS', [])
    settings.ADDL_INSTALLED_APPS.append('custom_user_fields')

def plugin_urls(urlpatterns):
    from django.conf.urls import url, include
    urlpatterns.append(url(r'', include('custom_user_fields.urls')))