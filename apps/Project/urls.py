from django.urls import path, include 
from apps.Project.views import ProjectViewSet, ProjectTagViewSet, MileStoneViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('project_tag', ProjectTagViewSet, basename='project-tag')
router.register('project', ProjectViewSet, basename='project')
router.register('milestone', MileStoneViewSet, basename='milestone')

urlpatterns = [
 path('', include(router.urls))
]