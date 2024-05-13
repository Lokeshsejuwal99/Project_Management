from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Task.views import TaskViewSet, InventoryTaskViewSet, EquipmentsTaskViewSet, EmployeeAssignedTaskViewSet

router = DefaultRouter()
router.register('Tasks', TaskViewSet, basename='task')
router.register('Employees_task', EmployeeAssignedTaskViewSet, basename='Employees-task')
router.register('Equipements_task', EquipmentsTaskViewSet, basename='Equipements-task')
router.register('Inventory', InventoryTaskViewSet, basename='inventory')


urlpatterns = [
    path('', include(router.urls))
]
