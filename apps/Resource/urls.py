from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryViewSet, EquipementsViewSet, EmployeeViewSet, BudgetViewSet

router = DefaultRouter()
router.register('Inventory', InventoryViewSet, basename='Inventory')
router.register('Equipment', EquipementsViewSet, basename='Equipment')
router.register('Employee', EmployeeViewSet, basename='Employee')
router.register('Budget', BudgetViewSet, basename='Budget')

urlpatterns = [
    path('', include(router.urls))
]
