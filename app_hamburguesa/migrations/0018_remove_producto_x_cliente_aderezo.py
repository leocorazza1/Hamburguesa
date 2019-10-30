# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hamburguesa', '0017_remove_producto_x_cliente_estaencarrito'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto_x_cliente',
            name='aderezo',
        ),
    ]
