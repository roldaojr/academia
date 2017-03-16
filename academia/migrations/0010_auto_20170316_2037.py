# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0009_auto_20170316_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dobra',
            name='metodo',
            field=models.CharField(choices=[('pestroski_1995_mulher', 'Pestroski 1995 (mulheres, 18 a 61 anos)'), ('durnin_womersley_1974', 'Durnin Womersley 1974'), ('jackson_pollock_ward_1980', 'Jackson, Pollock e Ward 1980 (mulheres, 18 a 55 anos)'), ('jackson_pollock_1978', 'Jackson, Pollock 1984'), ('pollock_schimidt_jackson_1980', 'Pollock, Schimidt e Jackson 1980 (adultos)'), ('jackson_pollock_ward_1984', 'Jackson, Pollock e Ward 1984'), ('pestroski_1995_homem', 'Pestroski 1995 (homens, 18 a 61 anos)')], max_length=50),
        ),
    ]
