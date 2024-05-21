from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Project_main API",
        default_version="v1",
        description="APIs endpoint for project management.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sejuwallokesh77@gmail.com"),
        license=openapi.License(name="lokeshsejuwal")
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    path('PM/project/', include('apps.Project.urls')),
    path('PM/task/', include('apps.Task.urls')),
    path('PM/resource/', include('apps.Resource.urls')),
    path('PM/effort/', include('apps.Effort.urls')),
    path('PM/report/', include('apps.Report.urls')),
    path('PM/admin/', admin.site.urls),
    path('PM/swagger/<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('PM/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('PM/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
    path('', RedirectView.as_view(url='/PM/project/', permanent=True)), 
]

urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)