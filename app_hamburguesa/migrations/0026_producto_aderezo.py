# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hamburguesa', '0025_remove_producto_x_cliente_aderezo'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='aderezo',
            field=models.ManyToManyField(to='app_hamburguesa.aderezo', blank=True, null=True),
        ),
    ]
