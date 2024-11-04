from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from restapp1.views import BlogPostViewSet


router = DefaultRouter()
router.register(r'blogposts', BlogPostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'restapp1'), namespace='api')),
]
