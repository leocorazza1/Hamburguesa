# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hamburguesa', '0002_remove_producto_x_cliente_encarrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto_x_cliente',
            name='estaencarrito',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
