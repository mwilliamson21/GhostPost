"""Ghosts URL Configuration

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
from Ghosts import views
# from Ghosts.models import Post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('addBoast_Roast/', views.add_post, name='addPost'),
    path('up_votes/<int:id>', views.up_votes),
    path('down_votes/<int:id>', views.down_votes),
    path('boast/', views.boast, name='boast'),
    path('roast/', views.roast, name='roast'),
]
