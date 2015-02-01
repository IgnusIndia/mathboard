# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20150201_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='description',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
