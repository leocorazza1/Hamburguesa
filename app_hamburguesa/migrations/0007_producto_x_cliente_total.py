# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hamburguesa', '0006_auto_20190729_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto_x_cliente',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
