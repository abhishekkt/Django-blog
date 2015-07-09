# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_blogger_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='username',
            field=models.CharField(default=b'username', unique=True, max_length=200),
        ),
    ]
