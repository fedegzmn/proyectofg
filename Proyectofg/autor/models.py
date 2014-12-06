from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ProfileAuthor(models.Model):
    user = models.ForeignKey(User)
    descripcion = models.TextField(max_length=180)

    def __unicode__(self):
        return "%s" % (self.user.get_full_name(),)