"""quickbook URL Configuration

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


urlpatterns = [
    path('', include('cal.urls', namespace='main_cal')),
    path('admin/', admin.site.urls),
    path('salon/', include('salon.urls', namespace='salon')),
    path('cal/', include('cal.urls')),
    path('cal2/', include('cal2.urls')),
    path('prices/', include('prices.urls', namespace='prices')),
    path('users/', include('users.urls', namespace='users')),
    path('accounts/', include('django.contrib.auth.urls')),
]
