from django.contrib import admin
from tweet_vote.models import TweetVote

# Custom admin action to call delete() on each TweetVote model
def delete_each(modeladmin, request, queryset):
	for vote in queryset:
		vote.delete()
delete_each.short_description = 'Delete each selected tweet vote'

class TweetVoteAdmin(admin.ModelAdmin):
	list_display = ('tweet', 'love')	
	actions = [delete_each]
	
admin.site.register(TweetVote, TweetVoteAdmin)