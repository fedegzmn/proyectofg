import datetime
from django.db import models
from autor.models import ProfileAuthor


# Create your models here.

class Post(models.Model):
    """
    Model to represent the blog posts.
    """
    author = models.ForeignKey(ProfileAuthor)
    message = models.TextField(max_length=1400)
    date_posted = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return "Autor: %s, Post: %s" % (self.author.username, self.message,)
