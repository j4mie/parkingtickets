from django.contrib import admin
from twitter_search_sync.models import Tweet

class TweetAdmin(admin.ModelAdmin):
	date_hierarchy = 'pub_time'
	list_display = ('upvotes', 'downvotes', 'user', 'pub_time', 'text')	
	ordering = ['-upvotes']
	
admin.site.register(Tweet, TweetAdmin)