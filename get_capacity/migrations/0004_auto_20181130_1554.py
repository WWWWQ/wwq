# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_capacity', '0003_capacitydata_ip'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TaskLog',
        ),
        migrations.DeleteModel(
            name='TaskResult',
        ),
    ]
