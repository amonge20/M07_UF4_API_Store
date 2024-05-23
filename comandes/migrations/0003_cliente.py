# Generated by Django 4.2.13 on 2024-05-23 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comandes', '0002_comanda_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]