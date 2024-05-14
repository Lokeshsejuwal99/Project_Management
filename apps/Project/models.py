from django.db import models
from multiupload.fields import MultiFileField
# Create your models here.


class ProjectTag(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name


class Project(models.Model):
    '''Models to represent a project plannigs.'''

    Priority = (
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("Urgent", "Urgent"),
    )

    Status = (
        ("Not Started", "Not Started"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
        ("On Hold", "On Hold"),
        ("Cancelled", "Cancelled"),
        ("Overdue", "Overdue"),
    )

    project_tag = models.ForeignKey(ProjectTag, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    Description = models.CharField(max_length=100)
    Start_date = models.DateField(auto_now_add=True)
    End_date = models.DateField()
    Priority = models.CharField(max_length=20, choices=Priority)
    Inventory = models.ManyToManyField('Resource.Inventory')
    Equipments = models.ManyToManyField('Resource.Equipments')
    Assigned_members = models.ManyToManyField('Resource.Employee_assigned')
    Status = models.CharField(max_length=20, choices=Status)
    Last_updated = models.DateField(auto_now_add=True, blank=True, null=True)
    Milestones = models.ManyToManyField('MileStone', blank=True, related_name='projects')
    Dependencies = models.ManyToManyField('Dependencies', related_name='dependencies')
    
    def __str__(self):
        return self.Name


class MileStone(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    Description = models.CharField(max_length=100)
    Start_date = models.DateField(auto_now_add=True)
    Deadline = models.DateField()

    def __str__(self):
        return self.Name

class Dependencies(models.Model): 
    task_dependencies = models.ForeignKey('Task.Task', on_delete=models.CASCADE)
    inventory_dependencies = models.ForeignKey('Resource.Inventory', on_delete=models.CASCADE)
    equipment_dependencies = models.ForeignKey('Resource.Equipments', on_delete=models.CASCADE)
    hr_dependencies = models.ForeignKey('Resource.Employee_assigned', on_delete=models.CASCADE)

    def __int__(self):
        return self.task_dependencies


class UploadedFile(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None)
    files = models.FileField(upload_to='uploads/')
    