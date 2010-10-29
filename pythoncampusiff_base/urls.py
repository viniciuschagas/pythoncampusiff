from django.conf.urls.defaults import *

urlpatterns = patterns('pythoncampusiff_base.views',
    (r'^$', 'index'),
    (r'^local/$', 'local'),
    (r'^equipe/$', 'equipe'),
    (r'^equipe_do_site/$', 'equipe_do_site'),
)