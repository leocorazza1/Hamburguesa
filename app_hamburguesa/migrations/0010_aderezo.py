# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hamburguesa', '0009_carrito_producto_x_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='aderezo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=30, blank=True, null=True)),
            ],
        ),
    ]
