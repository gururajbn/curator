# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_products_curated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(max_length=50, choices=[(b'electronics', b'Electronics'), (b'fashion', b'Fashion'), (b'food', b'Food'), (b'travel', b'Travel')]),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.URLField(),
        ),
    ]
