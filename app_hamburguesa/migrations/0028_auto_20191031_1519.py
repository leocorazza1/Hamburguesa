# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hamburguesa', '0027_producto_x_cliente_tiempo_estimado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto_x_cliente',
            name='tiempo_estimado',
            field=models.CharField(null=True, blank=True, max_length=30),
        ),
    ]
