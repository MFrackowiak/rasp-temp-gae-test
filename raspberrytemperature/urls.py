from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
admin.autodiscover()

from raspberry_temperature import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'raspberrytemperature.views.home', name='home'),
    # url(r'^raspberrytemperature/', include('raspberrytemperature.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^temp/', csrf_exempt(views.basic_view)),
    url(r'^test/', csrf_exempt(views.test_view))
)
