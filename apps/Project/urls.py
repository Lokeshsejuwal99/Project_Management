from django.urls import path, include 
from apps.Project.views import ProjectViewSet, ProjectTagViewSet, MileStoneViewSet, EquipementsViewSet, InventoryViewSet, EmployeeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('project', ProjectViewSet, basename='project')
router.register('project_tag', ProjectTagViewSet, basename='project-tag')
router.register('milestone', MileStoneViewSet, basename='milestone')
router.register('employees', EmployeeViewSet, basename='employees')
router.register('inventory', InventoryViewSet, basename='inventory')
router.register('equipements', EquipementsViewSet, basename='equipements')


urlpatterns = [
 path('', include(router.urls))
]