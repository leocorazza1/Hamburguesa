# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hamburguesa', '0004_carrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='cliente',
            field=models.ForeignKey(null=True, to='app_hamburguesa.cliente', blank=True),
        ),
    ]
