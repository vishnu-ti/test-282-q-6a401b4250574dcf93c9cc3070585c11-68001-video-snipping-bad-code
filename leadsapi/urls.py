"""leadsapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from restapi.views import index, process_interval, \
    process_range, process_segments, combine_video, reset_db

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', index),
    path(r'api/process-interval', process_interval),
    path(r'api/process-range', process_range),
    path(r'api/process-segments', process_segments),
    path(r'api/combine-video', combine_video),
    path(r'api/reset-db/', reset_db),
]
