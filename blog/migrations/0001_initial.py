# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('title', models.CharField(unique=True, max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('body', models.TextField()),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('posted_on', models.DateField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='blogger',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('uid', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='posted_by',
            field=models.ForeignKey(to='blog.blogger'),
        ),
    ]
