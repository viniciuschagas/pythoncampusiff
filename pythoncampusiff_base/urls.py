from django.conf.urls.defaults import *

urlpatterns = patterns('pythoncampusiff_base.views',
    (r'^$', 'index'),
    (r'^local$', 'local'),
)