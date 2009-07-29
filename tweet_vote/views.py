from django.http import HttpResponse, HttpResponseRedirect
from twitter_search_sync.models import Tweet
from tweet_vote.models import TweetVote
from django.shortcuts import get_object_or_404

def vote(request, direction, object_id):
	if request.method == 'POST':
		tweet = get_object_or_404(Tweet, pk=object_id)
		
		if direction == 'love':
			choice = 1
		else: # direction must be 'irrelevant'
			choice = -1
		
		# Rudimentary avoidance of duplicate votes from the same user.	
		unique_key = request.session.session_key + ':' + request.META['REMOTE_ADDR']
			
		defaults = {
			'tweet': tweet,
			'vote': choice,
			'unique_key': unique_key,
		}
		
		obj, created = TweetVote.objects.get_or_create(unique_key = unique_key, tweet = tweet, defaults = defaults)			
		
		if created:
			response = 'success'
		else:
			response = 'already_voted'
			
		return HttpResponse(response)