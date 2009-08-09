# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from twitter_search_sync.models import Tweet
from django.db.models import Count
from django.db import models
import time
import datetime
import random
import math

# This is messy and unpleasant. Fix it.
class TweetSelector:

	_show_posts_from_last_n_days = 2
		
	def _get_random_from_queryset(self, queryset):
		count = queryset.count()
		if count == 0:
			return False
		else:
			random_tweet = queryset[random.randint(0, count-1)]
			return random_tweet
		
	def _get_quartic_from_sorted_queryset(self, queryset):
		count = queryset.count()
		if count == 0:
			return False
		else:
			index = int(math.pow(random.random(), 4) * count)
			return queryset[index]
		
	def _remove_irrelevant(self, queryset):
		return queryset.filter(irrelevant_count__lt=1)
		
	def _remove_voted_already(self, queryset):
		if self._voted_already:
			return queryset.exclude(id__in=self._voted_already)
		else:
			return queryset
		
	def _filter_queryset(self, queryset):
		filtered = self._remove_irrelevant(queryset)
		filtered = self._remove_voted_already(filtered)
		return filtered
	
	def _get_recent_tweet(self): 
		end_time = datetime.datetime.now()
		start_time = end_time - datetime.timedelta(days=2)
		
		recent_tweets = Tweet.objects.filter(
			pub_time__range = (start_time, end_time)
		).order_by('view_count')
		
		filtered = self._filter_queryset(recent_tweets)
		return self._get_quartic_from_sorted_queryset(filtered)
		
	def _get_high_scoring_tweet(self):
		#sorted = Tweet.objects.filter(normalised_love__gt=0.8)
		sorted = Tweet.objects.filter(
			normalised_love__gt=0.3
		).order_by(
			'normalised_love'
		)
		filtered = self._filter_queryset(sorted)
		#to_return = self._get_random_from_queryset(filtered)
		return self._get_quartic_from_sorted_queryset(filtered)
	
	def get_tweet_to_display(self, voted_already):
	
		self._voted_already = voted_already
		
		selection_methods = [
			self._get_recent_tweet,
			self._get_high_scoring_tweet,
		]
		
		random.shuffle(selection_methods)
		
		for method in selection_methods:
			print method
			tweet = method()
			if tweet: return tweet
		
		return False
	
def homepage(request):
	voted_already = request.session.get('voted_tweets', [])

	selector = TweetSelector()
	tweet_to_display = selector.get_tweet_to_display(voted_already)
	
	if not tweet_to_display:
		return render_to_response('parkingtickets/notweets.html')
	
#	voted_already.append(tweet_to_display.id)
#	request.session['voted_tweets'] = voted_already
	
	# Log this view
	Tweet.objects.filter(id=tweet_to_display.id).update(view_count = models.F('view_count') + 1)
	
	return render_to_response('parkingtickets/homepage.html', {'tweet': tweet_to_display})