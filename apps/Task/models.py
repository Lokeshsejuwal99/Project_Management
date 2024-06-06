from django.db import models
# Create your models here.

Priority = (("Low", "Low"),
            ("Medium", "Medium"),
            ("High", "High"),
            ("Urgent", "Urgent"))

Status = (("Not Started", "Not Started"),
          ("In Progress", "In Progress"),
          ("Completed", "Completed"),
          ("On Hold", "On Hold"),
          ("Cancelled", "Cancelled"),
          ("Overdue", "Overdue"))


class Task(models.Model):
    Project = models.ForeignKey('Project.Project', on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    Description = models.CharField(max_length=300)
    Start_date = models.DateField(auto_now_add=True)
    End_date = models.DateField()
    Priority = models.CharField(max_length=20, choices=Priority)
    Inventory = models.ManyToManyField('Resource.Inventory')
    Equipments = models.ManyToManyField('Resource.Equipments')
    Assigned_members = models.ManyToManyField('Resource.Employee_assigned')
    Status = models.CharField(max_length=20, choices=Status)
    Last_updated = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.Name


class SubTask(models.Model):
    Task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE, null=True)
    Name = models.CharField(max_length=30)
    Description = models.CharField(max_length=300)
    Start_date = models.DateField(auto_now_add=True)
    End_date = models.DateField()
    Priority = models.CharField(max_length=20, choices=Priority)
    Inventory = models.ManyToManyField('Resource.Inventory')
    Equipments = models.ManyToManyField('Resource.Equipments')
    Assigned_members = models.ManyToManyField('Resource.Employee_assigned')
    Status = models.CharField(max_length=20, choices=Status)
    Last_updated = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.Name