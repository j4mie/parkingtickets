from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^admin/', include(admin.site.urls)),
    (r'^vote/', include('tweet_vote.urls')),
    (r'^static_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
    (r'^help/', direct_to_template, {'template': 'parkingtickets/help.html'}, 'help-page'),
    (r'^', include('parkingtickets.urls')),
    
)
