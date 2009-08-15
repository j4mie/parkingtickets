from django.conf.urls.defaults import *
from twitter_search_sync.models import Tweet

urlpatterns = patterns('parkingtickets.views',
	(r'^$', 'homepage'),
	(r'^topten/', 'topten'),

)