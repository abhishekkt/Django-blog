# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20150710_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_by',
            new_name='blogger',
        ),
    ]
