# Generated by Django 5.1.3 on 2024-12-05 03:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cip_main', '0007_empleado'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subservicios', to='cip_main.servicio'),
        ),
    ]
