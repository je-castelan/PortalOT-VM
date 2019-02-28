# Generated by Django 2.1.4 on 2019-02-28 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgenteCorreo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Agente de correo',
            },
        ),
        migrations.AlterModelOptions(
            name='ejecutor',
            options={'verbose_name_plural': 'Ejecutores'},
        ),
    ]