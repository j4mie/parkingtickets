from django.contrib import admin
from tweet_vote.models import TweetVote

class TweetVoteAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'vote', 'tweet')	
	list_filter = ('vote',)
	
admin.site.register(TweetVote, TweetVoteAdmin)