from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from twitter_search_sync.models import Tweet
from tweet_vote.models import TweetVote
from django.shortcuts import get_object_or_404

def vote(request, object_id):
	if request.method == 'POST':
		tweet = get_object_or_404(Tweet, pk=object_id)
		
		# Validate love parameter
		if not 'vote' in request.POST:
			return HttpResponseBadRequest('A Love Supreme')
		
		try:
			love = float(request.POST['vote'])
		except:
			return HttpResponseBadRequest("You Don't Know What Love Is")
		
		if love < 0 or love > 1:
			return HttpResponseBadRequest("This Can't Be Love")
				
		# Rudimentary avoidance of duplicate votes from the same user.	
		unique_key = request.session.session_key
			
		defaults = {
			'tweet': tweet,
			'love': love,
			'unique_key': unique_key,
		}
		
		obj, created = TweetVote.objects.get_or_create(unique_key = unique_key, tweet = tweet, defaults = defaults)			
		
		if created:
			response = HttpResponse('success')
			voted_on = request.session['voted_tweets']
			voted_on.append(tweet.id)
			request.session['voted_tweets'] = voted_on
		else:
			response = HttpResponseForbidden('already_voted')
			
		return response
	