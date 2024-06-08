from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.WorkSpace.views import WorkSpaceViewSet


router = DefaultRouter()
router.register('workspace', WorkSpaceViewSet, basename='workspace')
urlpatterns = [
    path('', include(router.urls))
]