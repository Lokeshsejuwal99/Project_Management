# Generated by Django 5.0.4 on 2024-05-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
        ('Resource', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipments',
            name='Assigned_to',
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
        migrations.AlterField(
            model_name='project',
            name='Assigned_members',
            field=models.ManyToManyField(to='Resource.employee_assigned'),
        ),
        migrations.AlterField(
            model_name='project',
            name='Equipments',
            field=models.ManyToManyField(to='Resource.equipments'),
        ),
        migrations.AlterField(
            model_name='project',
            name='Inventory',
            field=models.ManyToManyField(to='Resource.inventory'),
        ),
        migrations.DeleteModel(
            name='Employee_assigned',
        ),
        migrations.DeleteModel(
            name='Equipments',
        ),
    ]
