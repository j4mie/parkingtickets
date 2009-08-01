from django.db import models
from twitter_search_sync.models import Tweet
from datetime import datetime

# Create your models here.
class TweetVote(models.Model):
	
	VOTE_CHOICES = (
		(1, u'LOVE'),
		(-1, u'IRRELEVANT'),
	)
	
	tweet = models.ForeignKey(Tweet)
	vote = models.SmallIntegerField(choices=VOTE_CHOICES)
	unique_key = models.TextField()
	voted_at = models.DateTimeField(default=datetime.now())
	
	def __unicode__(self):
		return self.tweet.user + ': ' + self.get_vote_display()
		
	def save(self, *args, **kwargs):
		if self.vote == 1:
			Tweet.objects.filter(pk = self.tweet.pk).update(upvotes = models.F('upvotes') + 1)
		if self.vote == -1:
			Tweet.objects.filter(pk = self.tweet.pk).update(downvotes = models.F('downvotes') + 1)
		super(TweetVote, self).save(*args, **kwargs)
		
	def delete(self):
		if self.vote == 1:
			Tweet.objects.filter(pk = self.tweet.pk).update(upvotes = models.F('upvotes') - 1)
		if self.vote == -1:
			Tweet.objects.filter(pk = self.tweet.pk).update(downvotes = models.F('downvotes') -1)
		super(TweetVote, self).delete()