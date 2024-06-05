from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ProjectTagViewSet, MileStoneViewSet, DependenciesViewSet, WorkSpaceViewSet, GanttChartViewSet

router = DefaultRouter()
router.register('workspace', WorkSpaceViewSet, basename='workspace')
router.register('project_tag', ProjectTagViewSet, basename='project-tag')
router.register('project', ProjectViewSet, basename='project')
router.register('milestone', MileStoneViewSet, basename='milestone')
router.register('dependencies', DependenciesViewSet, basename='dependencies')
# router.register('ganttchart', GanttChartViewSet, basename='ganttchart')

urlpatterns = [
    path('', include(router.urls)), 
    path('ganttchart/', GanttChartViewSet.as_view())
]