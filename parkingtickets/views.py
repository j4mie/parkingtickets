# Create your views here.
from django.shortcuts import render_to_response
from twitter_search_sync.models import Tweet
from django.db.models import Count
from random import randint

def homepage(request):
	tweets = Tweet.objects.filter(downvotes__lt=5)
	tweet_count = tweets.count()
	random_tweet = tweets[randint(0, tweet_count-1)]
	request.session['parkingticket'] = True
	return render_to_response('parkingtickets/homepage.html', {'tweet': random_tweet})