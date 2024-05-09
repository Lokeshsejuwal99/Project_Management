from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryViewSet, EquipementsViewSet, EmployeeViewSet

router = DefaultRouter()
router.register('inventory', InventoryViewSet, basename='inventory')
router.register('equipment', EquipementsViewSet, basename='equipment')
router.register('employee', EmployeeViewSet, basename='employee')

urlpatterns = [
 path('', include(router.urls))
]
