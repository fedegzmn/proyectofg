# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileauthor',
            name='descripcion',
            field=models.TextField(max_length=200),
            preserve_default=True,
        ),
    ]
