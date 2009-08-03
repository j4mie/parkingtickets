from django.http import HttpResponse, HttpResponseForbidden
from twitter_search_sync.models import Tweet
from tweet_vote.models import TweetVote
from django.shortcuts import get_object_or_404

def vote(request, direction, object_id):
	if request.method == 'POST':
		tweet = get_object_or_404(Tweet, pk=object_id)
		
		if direction == 'love':
			choice = 1
		elif direction == 'irrelevant':
			choice = -1
		else: # must be 'ignore'
			choice = 0
		
		# Rudimentary avoidance of duplicate votes from the same user.	
		unique_key = request.session.session_key
			
		defaults = {
			'tweet': tweet,
			'vote': choice,
			'unique_key': unique_key,
		}
		
		obj, created = TweetVote.objects.get_or_create(unique_key = unique_key, tweet = tweet, defaults = defaults)			
		
		if created:
			response = HttpResponse('success')
		else:
			response = HttpResponseForbidden('already_voted')
			
		return response