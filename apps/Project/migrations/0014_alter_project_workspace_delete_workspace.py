# Generated by Django 4.2.13 on 2024-06-07 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WorkSpace', '0001_initial'),
        ('Project', '0013_alter_dependencies_task_dependencies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='WorkSpace',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='WorkSpace.workspace'),
        ),
        migrations.DeleteModel(
            name='WorkSpace',
        ),
    ]
