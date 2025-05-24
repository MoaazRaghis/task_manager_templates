"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todos.views import TodoViewSet
from users import views
from users.views import LoginView, ProfileView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todos.views import TodoViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')  # Add basename

urlpatterns = [
    path('', include(router.urls)),
]
router = DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', include(router.urls)),
]
