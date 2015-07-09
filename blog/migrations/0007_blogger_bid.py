# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_comment_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogger',
            name='bid',
            field=models.CharField(default=b'0', unique=True, max_length=50),
        ),
    ]
