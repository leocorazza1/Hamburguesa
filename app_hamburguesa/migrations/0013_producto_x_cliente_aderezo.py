# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hamburguesa', '0012_remove_producto_x_cliente_aderezo'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto_x_cliente',
            name='aderezo',
            field=models.ManyToManyField(blank=True, to='app_hamburguesa.aderezo', null=True),
        ),
    ]
