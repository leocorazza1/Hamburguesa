# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hamburguesa', '0005_carrito_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrito',
            old_name='cliente',
            new_name='clienteC',
        ),
        migrations.RenameField(
            model_name='carrito',
            old_name='producto',
            new_name='productoC',
        ),
    ]
