# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150913_0700'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='curated',
            field=models.BooleanField(default=False),
        ),
    ]
