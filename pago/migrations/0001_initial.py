# Generated by Django 4.2.11 on 2024-05-23 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comandes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_tarjeta', models.CharField(max_length=16)),
                ('fecha_caducidad', models.CharField(max_length=5)),
                ('cvc', models.CharField(max_length=3)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_pago', models.DateTimeField(auto_now_add=True)),
                ('comanda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='comandes.comanda')),
            ],
        ),
    ]
