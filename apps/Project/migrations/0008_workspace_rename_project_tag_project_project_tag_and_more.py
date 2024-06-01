# Generated by Django 4.2.13 on 2024-06-01 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0007_projectfile_remove_project_files_delete_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Workspace_name', models.CharField(max_length=100)),
                ('Priority', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Urgent', 'Urgent')], max_length=20)),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_tag',
            new_name='Project_tag',
        ),
        migrations.RenameField(
            model_name='projecttag',
            old_name='name',
            new_name='Name',
        ),
    ]
