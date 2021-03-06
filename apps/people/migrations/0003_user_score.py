# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20141214_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.FloatField(default=0, help_text='Current score; decays every 10 minutes.'),
            preserve_default=True,
        ),
    ]
