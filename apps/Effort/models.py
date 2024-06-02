from django.db import models
from apps.Task.models import Task 
from apps.Project.models import Project
# from auth_mgmt.models import CustomUser
# Create your models here.

class EffortCalculation(models.Model):
 # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
 task = models.ForeignKey(Task, on_delete=models.CASCADE)
 project = models.ForeignKey(Project, on_delete=models.CASCADE)
 start_time = models.DateField()
 end_time = models.DateField()
 remind = models.CharField(max_length=100)
 notes = models.TextField()

 def add_dynamic_field(self, field_name, field_value):
  self.dynamic_fields[field_name] = field_value 
 