# Generated by Django 3.1.3 on 2020-12-20 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20201219_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmation',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='confirmation',
            name='landmark',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='confirmation',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='confirmation',
            name='state',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='ecommerce',
            name='image',
            field=models.CharField(max_length=1000),
        ),
    ]
