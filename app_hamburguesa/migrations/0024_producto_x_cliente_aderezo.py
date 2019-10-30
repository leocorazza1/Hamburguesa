# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hamburguesa', '0023_auto_20191030_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto_x_cliente',
            name='aderezo',
            field=models.ManyToManyField(null=True, to='app_hamburguesa.aderezo', blank=True),
        ),
    ]
