from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from edmin_test.views import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^cinema/add$', cinema_add, name='cinema-add'),
    url(r'^cinema/(?P<cinema_id>\d+)/edit$', cinema_edit, name='cinema-edit'),
    url(r'^cinema/(?P<cinema_id>\d+)/delete$', cinema_delete, name='cinema-delete'),
    url(r'^cinema/(?P<cinema_id>\d+)/(?P<presentations_date>[^/]+)/add$', presentation_add, name='presentation-add'),
    url(r'^cinema/(?P<cinema_id>\d+)/(?P<presentations_date>[^/]+)?$', cinema, name='cinema'),
    url(r'^cinema/(?P<cinema_id>\d+)/(?P<presentations_date>[^/]+)/(?P<presentation_id>\d+)/delete$', 
        presentation_delete, 
        name='presentation-delete'),
    # url(r'^admin/', include(admin.site.urls)),
)
