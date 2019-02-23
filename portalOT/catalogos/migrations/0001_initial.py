# Generated by Django 2.1.4 on 2019-02-22 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ejecutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Gerencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, unique=True)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('clli', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('localidad', models.CharField(max_length=25)),
                ('ubicacion', models.CharField(max_length=75)),
                ('codigo', models.CharField(max_length=4)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('codigo', models.CharField(max_length=4)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('telefono', models.CharField(max_length=10)),
                ('activo', models.BooleanField()),
                ('gerencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.Gerencia')),
            ],
        ),
        migrations.AddField(
            model_name='ejecutor',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.Proveedor'),
        ),
    ]