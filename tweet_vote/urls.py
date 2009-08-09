from django.conf.urls.defaults import *
from twitter_search_sync.models import Tweet

urlpatterns = patterns('tweet_vote.views',
	(r'^(?P<object_id>\d+)/?$', 'vote'),
)