# Generated by Django 4.2.13 on 2024-06-01 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0004_remove_subtask_project_subtask_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='project',
            new_name='Project',
        ),
    ]
