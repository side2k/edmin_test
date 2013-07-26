from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from edmin_test.views import index
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    # url(r'^admin/', include(admin.site.urls)),
)
