"""AUVSI_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from controlcenter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.connectionPage,name='connectionPage'),
    path('controlCenter',views.controlCenter,name='controlCenter'),
    path('get_mission',views.getMission,name='mission'),
    path('upload_mission', views.uploadMission, name='uploadMission'),
    path('boundaryGrid',views.boundaryGrid,name='boundaryGrid'),
    path('wayPointsGrid',views.wayPointsGrid,name='wayPointsGrid'),
]
