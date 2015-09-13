# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='selected',
            options={'ordering': ['-time']},
        ),
        migrations.AddField(
            model_name='selected',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
