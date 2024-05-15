from django.urls import path, include
from apps.Project.views import ProjectViewSet, ProjectTagViewSet, MileStoneViewSet, DependenciesViewSet, FileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('project', ProjectViewSet, basename='project')
router.register('project_tag', ProjectTagViewSet, basename='project-tag')
router.register('milestone', MileStoneViewSet, basename='milestone')
router.register('dependencies', DependenciesViewSet, basename='dependencies')
router.register('upload', FileViewSet, basename='upload-files')

urlpatterns = [
    path('', include(router.urls))
    ]
