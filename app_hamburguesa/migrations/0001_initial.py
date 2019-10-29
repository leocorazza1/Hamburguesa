# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(null=True, max_length=20, blank=True)),
                ('apellido', models.CharField(null=True, max_length=20, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('contacto', models.CharField(null=True, max_length=20, blank=True)),
                ('cuenta_usuario', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(null=True, max_length=100, blank=True)),
                ('descripcion', models.CharField(null=True, max_length=200, blank=True)),
                ('precio', models.FloatField(null=True, blank=True)),
                ('stock', models.IntegerField(null=True, blank=True)),
                ('tipo', models.CharField(null=True, max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='producto_x_cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(null=True, blank=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('hora', models.TimeField(null=True, blank=True)),
                ('direccion', models.CharField(null=True, max_length=30, blank=True)),
                ('encarrito', models.IntegerField(null=True, blank=True)),
                ('cliente', models.ForeignKey(null=True, to='app_hamburguesa.cliente', blank=True)),
                ('producto', models.ForeignKey(null=True, to='app_hamburguesa.producto', blank=True)),
            ],
        ),
    ]
