# Generated by Django 4.2.13 on 2024-05-24 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Effort', '0002_alter_effortcalculation_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effortcalculation',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
