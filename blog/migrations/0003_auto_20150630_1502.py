# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150630_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='posted_by',
            new_name='blogger',
        ),
    ]
