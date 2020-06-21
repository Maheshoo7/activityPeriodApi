from django.contrib import admin
from django.urls import path, include
from Myapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include(router.urls)),

]
