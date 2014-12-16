# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0002_auto_20141215_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileauthor',
            name='nombre',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
