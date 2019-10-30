# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hamburguesa', '0013_producto_x_cliente_aderezo'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='url',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
