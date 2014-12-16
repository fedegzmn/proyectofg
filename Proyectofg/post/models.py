import datetime
from django.db import models
from autor.models import ProfileAuthor


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return "%s" % (self.name,)

class Post(models.Model):

    author = models.ForeignKey(ProfileAuthor)
    title = models.CharField(max_length=200)
    message = models.TextField()
    category =models.ForeignKey(Category)
    date_posted = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return "Autor: %s, Titulo: %s" % (self.author.nombre, self.title,)
