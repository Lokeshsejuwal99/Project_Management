# Generated by Django 4.2.13 on 2024-05-15 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Project', '0001_initial'),
        ('Resource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_assigned_Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_id', models.IntegerField()),
                ('Employee_name', models.CharField(max_length=30)),
                ('Employee_email', models.EmailField(max_length=254)),
                ('Employee_phone', models.IntegerField()),
                ('Employee_address', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory_Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Quantity', models.IntegerField()),
                ('size', models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], max_length=30)),
                ('Client_name', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=30)),
                ('Phone', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=300)),
                ('Start_date', models.DateField(auto_now_add=True)),
                ('End_date', models.DateField()),
                ('Priority', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Urgent', 'Urgent')], max_length=20)),
                ('Status', models.CharField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('On Hold', 'On Hold'), ('Cancelled', 'Cancelled'), ('Overdue', 'Overdue')], max_length=20)),
                ('Last_updated', models.DateField(auto_now_add=True, null=True)),
                ('Assigned_members', models.ManyToManyField(to='Task.employee_assigned_task')),
                ('Equipments', models.ManyToManyField(to='Resource.equipments')),
                ('Inventory', models.ManyToManyField(to='Resource.inventory')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.project')),
            ],
        ),
        migrations.CreateModel(
            name='Equipments_Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Equipement_id', models.IntegerField()),
                ('Equipment_name', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=100)),
                ('Quantity', models.IntegerField(default=1)),
                ('Condition', models.CharField(choices=[('New', 'New'), ('Used', 'Used'), ('Damaged', 'Damaged'), ('Broken', 'Broken')], max_length=20)),
                ('Assigned_to', models.ManyToManyField(blank=True, to='Task.employee_assigned_task')),
            ],
        ),
    ]
