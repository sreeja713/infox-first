# Generated by Django 4.0.3 on 2022-03-22 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='std_address',
            field=models.CharField(max_length=255),
        ),
    ]
