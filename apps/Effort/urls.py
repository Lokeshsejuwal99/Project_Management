from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Effort.views import EffortCalculationViewSet

router = DefaultRouter()
router.register('effort', EffortCalculationViewSet, basename='efforts')
urlpatterns = [
    path('', include(router.urls))
]
