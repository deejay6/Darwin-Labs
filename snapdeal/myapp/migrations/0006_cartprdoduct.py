# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20171005_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartPrdoduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catalogue_id', models.CharField(max_length=50, null=True)),
                ('cart', models.ForeignKey(to='myapp.Cart')),
                ('product', models.ForeignKey(to='myapp.Product')),
            ],
        ),
    ]
