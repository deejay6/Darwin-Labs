# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to='myapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='CartPrdoduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.CharField(max_length=100, null=True)),
                ('catalogue_id', models.CharField(max_length=50, null=True)),
                ('cart_id', models.ForeignKey(to='myapp.Cart')),
            ],
        ),
    ]
