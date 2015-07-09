# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20150709_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogger',
            name='username',
            field=models.CharField(default=b'none', max_length=200),
        ),
    ]
