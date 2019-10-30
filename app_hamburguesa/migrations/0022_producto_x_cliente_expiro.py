# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hamburguesa', '0021_remove_producto_x_cliente_expiro'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto_x_cliente',
            name='expiro',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=False,
        ),
    ]
