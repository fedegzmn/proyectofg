# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(max_length=1400)),
                ('date_posted', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(to='autor.ProfileAuthor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
