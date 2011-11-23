from django.conf.urls.defaults import *
from radio.views import index

urlpatterns = patterns('',
    (r'^$', index),
    (r'^register/$', 'radio.views.register'),
)