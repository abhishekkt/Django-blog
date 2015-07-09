# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150709_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='bid',
            field=models.IntegerField(default=0, serialize=False, primary_key=True),
        ),
    ]
