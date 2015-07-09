# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogger_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogger',
            name='bid',
        ),
    ]
