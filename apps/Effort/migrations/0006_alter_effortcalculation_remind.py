# Generated by Django 4.2.13 on 2024-06-01 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Effort', '0005_alter_effortcalculation_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effortcalculation',
            name='remind',
            field=models.CharField(max_length=100),
        ),
    ]
