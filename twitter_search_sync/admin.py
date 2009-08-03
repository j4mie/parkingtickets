from django.contrib import admin
from twitter_search_sync.models import Tweet

class TweetAdmin(admin.ModelAdmin):
	date_hierarchy = 'pub_time'
	list_display = ('love_count', 'irrelevant_count', 'ignore_count', 'view_count', 'user', 'pub_time', 'text')	
	ordering = ['-love_count']
	
admin.site.register(Tweet, TweetAdmin)