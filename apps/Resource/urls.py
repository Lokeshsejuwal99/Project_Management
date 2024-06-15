from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryViewSet, EquipementsViewSet, EmployeeViewSet, BudgetViewSet

router = DefaultRouter()
router.register('inventory', InventoryViewSet, basename='Inventory')
router.register('equipment', EquipementsViewSet, basename='Equipment')
router.register('employee', EmployeeViewSet, basename='Employee')
router.register('budget', BudgetViewSet, basename='Budget')

urlpatterns = [
    path('', include(router.urls))
]
