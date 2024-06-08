from django.db import models

# Create your models here.

Priority = (("Low", "Low"),
            ("Medium", "Medium"),
            ("High", "High"),
            ("Urgent", "Urgent"))


class WorkSpace(models.Model):
    Workspace_name = models.CharField(max_length=100)
    Priority = models.CharField(max_length=20, choices=Priority)
    created_on = models.DateField(auto_now_add=True)
    is_archive = models.BooleanField(default=False, null=True)
    is_bookmarked = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.Workspace_name
