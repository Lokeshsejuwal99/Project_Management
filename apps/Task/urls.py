from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Task.views import TaskViewSet, SubTaskViewSet

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='task')
router.register('subtasks', SubTaskViewSet, basename='Subtask')

urlpatterns = [
    path('', include(router.urls))
]
