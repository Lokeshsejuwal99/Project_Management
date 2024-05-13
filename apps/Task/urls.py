from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Task.views import TaskViewSet, InventoryTaskViewSet, EquipmentsTaskViewSet, EmployeeAssignedTaskViewSet

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='task')
router.register('employees_task', EmployeeAssignedTaskViewSet, basename='employees-task')
router.register('equipements_task', EquipmentsTaskViewSet, basename='equipements-task')
router.register('inventory', InventoryTaskViewSet, basename='inventory')


urlpatterns = [
    path('', include(router.urls))
]
