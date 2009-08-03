# Create your views here.
from django.shortcuts import render_to_response
from twitter_search_sync.models import Tweet
from django.db.models import Count
from django.db import models
from random import randint

def homepage(request):
	tweets = Tweet.objects.filter(irrelevant_count__lt=5)
	tweet_count = tweets.count()
	random_tweet = tweets[randint(0, tweet_count-1)]
	
	# Set a session variable. Allows us to track anon users by session ID
	request.session['parkingticket'] = True
	
	# Log this view
	Tweet.objects.filter(id=random_tweet.id).update(view_count = models.F('view_count') + 1)
	return render_to_response('parkingtickets/homepage.html', {'tweet': random_tweet})