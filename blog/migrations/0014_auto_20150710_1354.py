# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20150709_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blogger',
            new_name='blog_by',
        ),
    ]
