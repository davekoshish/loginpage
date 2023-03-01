# myproject/urls.py

from django.urls import path, include
from rest_framework import routers
from accounts.views import UserViewSet, LoginView

from django.contrib import admin
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
       path('admin/', admin.site.urls),
     path('login/', LoginView.as_view(), name='login'),
]
