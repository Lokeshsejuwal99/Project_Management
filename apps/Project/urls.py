from django.urls import path, include
from apps.Project.views import ProjectViewSet, ProjectTagViewSet, MileStoneViewSet, DependenciesViewSet
from rest_framework.routers import DefaultRouter
from . import views  

router = DefaultRouter()
router.register('project', ProjectViewSet, basename='project')
router.register('project_tag', ProjectTagViewSet, basename='project-tag')
router.register('milestone', MileStoneViewSet, basename='milestone')
router.register('dependencies', DependenciesViewSet, basename='dependencies')

urlpatterns = [
    path('', include(router.urls))
    ]
