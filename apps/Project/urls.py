from django.urls import path, include
from apps.Project.views import ProjectViewSet, ProjectTagViewSet, MileStoneViewSet, DependenciesViewSet, ProjectViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('project', ProjectViewSet, basename='project')
router.register('project_tag', ProjectTagViewSet, basename='project-tag')
router.register('milestone', MileStoneViewSet, basename='milestone')
router.register('dependencies', DependenciesViewSet, basename='dependencies')
router.register(r'upload', ProjectViewSet, basename='file-upload')

urlpatterns = [
    path('', include(router.urls)),
    path('upload/multiple/', ProjectViewSet.as_view({'post': 'upload_multiple_files'}), name='upload-multiple-files')
    ]
