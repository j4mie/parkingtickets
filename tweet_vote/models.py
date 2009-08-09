from django.db import models
from twitter_search_sync.models import Tweet
from datetime import datetime

# Create your models here.
class TweetVote(models.Model):
	
	tweet = models.ForeignKey(Tweet)
	love = models.FloatField()
	unique_key = models.TextField()
	voted_at = models.DateTimeField(default=datetime.now())
	
	# Update denormalised fields on tweet model
	# Direction must be +1 or -1
	# WARNING: THIS METHOD IS FULL OF RACE CONDITIONS.
	def update_tweet(self, direction):		
		self.tweet.total_love += self.love * direction
		self.tweet.vote_count = self.tweet.vote_count + direction
		self.tweet.normalised_love = self.tweet.total_love / self.tweet.vote_count
		self.tweet.save()
		
	def save(self, *args, **kwargs):
		self.update_tweet(+1)
		super(TweetVote, self).save(*args, **kwargs)
		
	def delete(self):
		self.update_tweet(-1)
		super(TweetVote, self).delete()