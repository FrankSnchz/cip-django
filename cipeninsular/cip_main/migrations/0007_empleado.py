# Generated by Django 5.1.3 on 2024-12-03 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cip_main', '0006_remove_projectimage_producto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('posicion', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='empleados/')),
            ],
        ),
    ]
