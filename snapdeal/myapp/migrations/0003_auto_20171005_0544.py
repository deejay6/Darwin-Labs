# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_cart_cartprdoduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartprdoduct',
            old_name='cart_id',
            new_name='cart',
        ),
    ]
