# Generated by Django 4.2.13 on 2024-05-15 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True 

    dependencies = [
        ('Resource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_dependencies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resource.equipments')),
                ('hr_dependencies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resource.employee_assigned')),
                ('inventory_dependencies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resource.inventory')),
            ],
        ),
        migrations.CreateModel(
            name='MileStone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=100)),
                ('Start_date', models.DateField(auto_now_add=True)),
                ('Deadline', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=100)),
                ('Start_date', models.DateField(auto_now_add=True)),
                ('End_date', models.DateField()),
                ('Priority', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Urgent', 'Urgent')], max_length=20)),
                ('Status', models.CharField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('On Hold', 'On Hold'), ('Cancelled', 'Cancelled'), ('Overdue', 'Overdue')], max_length=20)),
                ('Last_updated', models.DateField(auto_now_add=True, null=True)),
                ('file', models.FileField(blank=True, default=None, null=True, upload_to='')),
                ('Assigned_members', models.ManyToManyField(to='Resource.employee_assigned')),
                ('Dependencies', models.ManyToManyField(related_name='dependencies', to='Project.dependencies')),
                ('Equipments', models.ManyToManyField(to='Resource.equipments')),
                ('Inventory', models.ManyToManyField(to='Resource.inventory')),
                ('Milestones', models.ManyToManyField(blank=True, related_name='milestone', to='Project.milestone')),
                ('project_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.projecttag')),
            ],
        ),
    ]
