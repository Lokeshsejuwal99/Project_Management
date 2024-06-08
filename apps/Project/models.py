from django.db import models
from multiupload.fields import MultiFileField
from apps.WorkSpace.models import WorkSpace

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


class ProjectTag(models.Model):
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name


class Project(models.Model):
    WorkSpace = models.ForeignKey(WorkSpace, on_delete=models.CASCADE, null=True)
    Project_tag = models.ForeignKey(ProjectTag, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    Description = models.CharField(max_length=700)
    Start_date = models.DateField(auto_now_add=True)
    End_date = models.DateField()
    Priority = models.CharField(max_length=20, choices=Priority)
    Inventory = models.ManyToManyField('Resource.Inventory')
    Equipments = models.ManyToManyField('Resource.Equipments')
    Assigned_members = models.ManyToManyField('Resource.Employee_assigned')
    Status = models.CharField(max_length=20, choices=Status)
    Last_updated = models.DateField(auto_now_add=True, blank=True, null=True)
    Milestones = models.ManyToManyField('Project.MileStone', blank=True, related_name='project_milestone')
    Dependencies = models.ManyToManyField('Project.Dependencies')
    is_archive = models.BooleanField(default=False, null=True)
    is_bookmarked = models.BooleanField(default=False, null=True)

    class Meta:
        ordering = ['Name']

    def __str__(self):
        return self.Name


class ProjectFile(models.Model):
    project = models.IntegerField()
    file = models.FileField(upload_to='uploads/', null=True, blank=True)

    def __int__(self):
        return self.project


class MileStone(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    Name = models.CharField(max_length=30)
    Description = models.CharField(max_length=100)
    Start_date = models.DateField(auto_now_add=True)
    Deadline = models.DateField()

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ['Name']


class Dependencies(models.Model):
    task_dependencies = models.ForeignKey('Task.Task', on_delete=models.CASCADE, related_name='dependencies', null=True)
    dependent_on = models.ForeignKey('Task.Task', related_name='dependents', on_delete=models.CASCADE, null=True)
    Inventory_dependencies = models.ForeignKey('Resource.Inventory', on_delete=models.CASCADE)
    Equipment_dependencies = models.ForeignKey('Resource.Equipments', on_delete=models.CASCADE)
    HR_dependencies = models.ForeignKey('Resource.Employee_assigned', on_delete=models.CASCADE)
    Buget_dependencies = models.ForeignKey('Resource.Budget', on_delete=models.CASCADE, null=True)
