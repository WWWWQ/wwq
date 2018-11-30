# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('iwork', '0002_auto_20180703_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workrecord',
            name='record_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 30, 15, 54, 38, 768247), verbose_name='\u4f1a\u8bae\u65f6\u95f4'),
        ),
    ]
