import time
from datetime import datetime
import feedparser
from django.utils.encoding import smart_unicode
from models import Tweet

class SearchSyncr:
	"""
	Sync a set of search results from the Twitter API with the database
	"""

	def __init__(self, searchstring):
		"""
		Create a new SearchSyncr instance
		
		searchstring should be a URL-encoded set of key-value pairs which
		will be passed to the Twitter search API
		"""
		
		self.searchurl = 'http://search.twitter.com/search.atom?q=' + searchstring
		self.created_count = 0

	def _syncTweet(self, entry):
		twitter_id = entry.id[entry.id.rindex(':')+1:]
		defaults = {
			'pub_time': datetime(*entry.published_parsed[:6]),
			'twitter_id': twitter_id,
			'user': smart_unicode(entry.author.split(' ')[0]),
			'text': smart_unicode(entry.title)
		}
		
		obj, created = Tweet.objects.get_or_create(twitter_id = twitter_id, defaults = defaults)
		if created: self.created_count += 1
		return obj

	def syncSearch(self):
		"""
		Run the SearchSyncr
		
		Returns the number of model objects that were created as part of the sync.
		"""
		searchfeed = feedparser.parse(self.searchurl)
		
		for tweet in searchfeed.entries:
			self._syncTweet(tweet)
			
		return self.created_count