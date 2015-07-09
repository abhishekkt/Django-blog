# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_blogger_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogger',
            name='uid',
        ),
        migrations.AddField(
            model_name='blogger',
            name='bid',
            field=models.CharField(default=b'None', max_length=30, serialize=False, primary_key=True),
        ),
    ]
