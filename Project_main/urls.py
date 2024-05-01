from django.contrib import admin
from django.urls import path, include, re_path
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
      license = openapi.License(name="lokeshsejuwal")
   ), 
public = True, 
permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
 path('project/', include('apps.Project.urls')),
 path('task/', include('apps.Task.urls')),
 path('resource/', include('apps.Resource.urls')),
 path('effort/', include('apps.Effort.urls')),
 path('report/', include('apps.Report.urls')),
 path('admin/', admin.site.urls),
 path('swagger/<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
 path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
 path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
