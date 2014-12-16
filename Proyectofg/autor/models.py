from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ProfileAuthor(models.Model):
    user = models.ForeignKey(User)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)

    def __unicode__(self):
        return "%s" % (self.nombre,)