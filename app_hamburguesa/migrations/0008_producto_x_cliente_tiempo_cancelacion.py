# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hamburguesa', '0007_producto_x_cliente_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto_x_cliente',
            name='tiempo_cancelacion',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
