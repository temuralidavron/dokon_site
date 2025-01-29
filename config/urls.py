
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Bu API uchun Swagger hujjatlari",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # ReDoc
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # JSON schema
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('admin/', admin.site.urls),
    path('',include('product.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
