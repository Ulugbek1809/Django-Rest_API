from django.urls import path, include
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="Test",
        license=openapi.License(name="Demo"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', booksviev.as_view(), name="APIlist"),
    path('all/', all.as_view({'get': 'list', "post": "list", "delete": "list", "put": "list"}), name="APIall"),
    path("detil/<int:pk>", bookdetail.as_view(), name="bookdetil"),
    path("delete/<int:pk>", bookdelete.as_view(), name="bookdelete"),
    path("updata/<int:pk>", bookupdata.as_view(), name="bookupdata"),
    path("create/", bookcreate.as_view(), name="bookcreate"),
    path("dj_rest_auth/", include("dj_rest_auth.urls")),
]
