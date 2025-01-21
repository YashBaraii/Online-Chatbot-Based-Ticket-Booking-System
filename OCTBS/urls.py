"""
URL configuration for OCTBS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# OCTBS/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views
from  .views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('interactive_maps/', views.interactive_maps, name='interactive_maps'),
    path('blog/', views.blog, name='blog'),
    path('store/', views.store, name='stores'),
    path('events/', views.events, name='eventss'),
    path('payment/', views.payments, name='payments'),
    path('success/', views.success, name='successs'),
    path('logout/', logout_view, name='logout'),

    path("__reload__/", include("django_browser_reload.urls")),
]