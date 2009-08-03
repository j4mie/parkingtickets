from django.db import models
from twitter_search_sync.models import Tweet
from datetime import datetime

# Create your models here.
class TweetVote(models.Model):
	
	VOTE_CHOICES = (
		(1, u'LOVE'),
		(-1, u'IRRELEVANT'),
		(0, u'IGNORE'),
	)
	
	DENORMALISED_FIELDS = {
		1 	: 'love_count',
		-1	: 'irrelevant_count',
		0 	: 'ignore_count'
	}
	
	tweet = models.ForeignKey(Tweet)
	vote = models.SmallIntegerField(choices=VOTE_CHOICES)
	unique_key = models.TextField()
	voted_at = models.DateTimeField(default=datetime.now())
	
	def __unicode__(self):
		return self.tweet.user + ': ' + self.get_vote_display()
	
	def update_vote(self, direction):
		field = self.DENORMALISED_FIELDS[self.vote]
		setattr(self.tweet, field, models.F(field) + direction)
		self.tweet.save()
		
	def save(self, *args, **kwargs):
		self.update_vote(+1)
		super(TweetVote, self).save(*args, **kwargs)
		
	def delete(self):
		self.update_vote(-1)
		super(TweetVote, self).delete()