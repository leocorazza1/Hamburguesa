# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hamburguesa', '0022_producto_x_cliente_expiro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto_x_cliente',
            name='expiro',
            field=models.BooleanField(default=False),
        ),
    ]
