from django.db import models
# Create your models here.

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


class ProjectTag(models.Model):
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name


class Project(models.Model):
    project_tag = models.ForeignKey(ProjectTag, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    Description = models.CharField(max_length=100)
    Start_date = models.DateField(auto_now_add=True)
    End_date = models.DateField()
    Priority = models.CharField(max_length=20, choices=Priority)
    Status = models.CharField(max_length=20, choices=Status)
    Last_updated= models.DateField(auto_now_add=True, blank=True, null=True)

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
    

