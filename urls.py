from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', include('pythoncampusiff_base.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^site_media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}
    ),
)
