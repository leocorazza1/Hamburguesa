# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hamburguesa', '0026_producto_aderezo'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto_x_cliente',
            name='tiempo_estimado',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
