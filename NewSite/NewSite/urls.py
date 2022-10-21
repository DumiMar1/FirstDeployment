"""NewSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from new_site_app import site_views
from pass_app import pass_views

urlpatterns = [
    path('', site_views.index, name='index'),
    path('pass_app/', include('pass_app.urls')),
    path('new_site_app/', include('new_site_app.urls')),
    path('admin/', admin.site.urls),
    path('logout/', pass_views.user_logout, name='logout'),

]
