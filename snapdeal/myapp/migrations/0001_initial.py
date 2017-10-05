# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SessionToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_token', models.CharField(max_length=255)),
                ('last_request_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('is_valid', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('username', models.CharField(unique=b'True', max_length=30)),
                ('age', models.IntegerField(null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='sessiontoken',
            name='user',
            field=models.ForeignKey(to='myapp.User'),
        ),
    ]
