# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hamburguesa', '0029_producto_x_cliente_referencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto_x_cliente',
            name='entregado',
            field=models.BooleanField(default=False),
        ),
    ]
