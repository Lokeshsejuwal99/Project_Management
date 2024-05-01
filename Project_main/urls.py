from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Project_main API",
      default_version="v1",
      description="APIs endpoint for project management.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="sejuwallokesh77@gmail.com"),
      license = openapi.License(license="lokeshsejuwal"), 
   ), 
public = True, 
permission_classes=(permissions.AllowAny, ),
), 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-swagger-format'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('project/', include('Project.urls')),
    path('task/', include('Task.urls')),
    path('resource/', include('resource.urls')),
    path('effort/', include('effort.urls')),
    path('report/', include('report.urls'))
]
