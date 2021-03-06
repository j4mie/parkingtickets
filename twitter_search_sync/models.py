from django.db import models
from django.conf import settings

# Somewhat based on code from http://code.google.com/p/django-syncr/
# Unpleasantly coupled to the voting app at the moment.

class BigIntegerField(models.IntegerField):
    """
    Defines a PostgreSQL compatible IntegerField needed to prevent 'integer 
    out of range' with large numbers.
    """
    def get_internal_type(self):
        return 'BigIntegerField'

    def db_type(self):
        if settings.DATABASE_ENGINE == 'oracle':
            db_type = 'NUMBER(19)'
        else:
            db_type = 'bigint'
        return db_type
        

class Tweet(models.Model):
    pub_time    = models.DateTimeField(db_index = True)
    twitter_id  = BigIntegerField(unique=True)
    text        = models.TextField()
    user        = models.TextField()
    real_name	= models.TextField()
    vote_count	= models.IntegerField(default = 0, db_index = True) # Denormalised
    total_love = models.FloatField(default = 0, db_index = True) # Denormalised
    normalised_love = models.FloatField(default = 0, db_index = True)
    
    irrelevant_count = models.IntegerField(default = 0, db_index = True)
    view_count	= models.IntegerField(default = 0, db_index = True)
    
    def __unicode__(self):
        return u'%s %s' % (self.user, self.pub_time)

    def url(self):
        return u'http://twitter.com/%s/statuses/%s' % (self.user, self.twitter_id)
        
    def user_url(self):
    	return u'http://twitter.com/%s' % self.user