from django.urls import path, include
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from .views import (
    ServiseViewSet,
    ClientViewSet,
    AdvisersViewSet,
    FeaturesViewSet,
    FAQsViewSet,
    CommentsViewSet
)

schema_view=get_schema_view(
    openapi.Info(
        title='spotify API docs',
        default_version='v1',
        description='API documentation',
        terms_of_service='https://www.gogle.com/policie/terms/',
        contact=openapi.Contact(email='contact@yourapi.local'),
        license=openapi.License(name='BSD license')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

router.register(r'serves', ServiseViewSet, basename='serves')
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'advisers', AdvisersViewSet, basename='advisers')
router.register(r'features', FeaturesViewSet, basename='features')
router.register(r'faqs', FAQsViewSet, basename='faqs')
router.register(r'comments', CommentsViewSet, basename='comments')


urlpatterns = [
    path('', include(router.urls)),
    path('api/token-auth/', include('rest_framework.urls')),
    path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
