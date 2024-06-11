# Generated by Django 5.0.6 on 2024-06-11 04:06

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.URLField(verbose_name='URL del logo')),
                ('nombre', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.categoria')),
            ],
        ),
    ]
