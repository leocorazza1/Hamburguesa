# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hamburguesa', '0028_auto_20191031_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto_x_cliente',
            name='referencia',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
