# Generated by Django 4.2.13 on 2024-05-16 15:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField(default=0)),
                ('creado_en', models.DateTimeField(default=django.utils.timezone.now)),
                ('actualizado_en', models.DateTimeField(auto_now=True)),
                ('eliminado', models.BooleanField(default=False)),
            ],
        ),
    ]
