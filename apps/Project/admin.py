from django.contrib import admin
from .models import Project, ProjectTag, MileStone, Dependencies, ProjectFile
# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectTag)
admin.site.register(MileStone)
admin.site.register(Dependencies)
admin.site.register(ProjectFile)