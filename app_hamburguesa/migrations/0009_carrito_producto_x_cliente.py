# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hamburguesa', '0008_producto_x_cliente_tiempo_cancelacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='producto_x_cliente',
            field=models.ForeignKey(blank=True, to='app_hamburguesa.producto_x_cliente', null=True),
        ),
    ]
