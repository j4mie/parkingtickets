from django.contrib import admin
from twitter_search_sync.models import Tweet

class TweetAdmin(admin.ModelAdmin):
	date_hierarchy = 'pub_time'
	list_display = ('normalised_love', 'vote_count', 'total_love', 'irrelevant_count', 'view_count', 'user', 'pub_time', 'text')	
	ordering = ['-normalised_love']
	search_fields = ['text','user','real_name']
	
admin.site.register(Tweet, TweetAdmin)