"""uretek URL Configuration

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

     re_path(r'(?P<slug>[-\w]+)/$', views.construction),
"""
from django.contrib import admin
from django.urls import path, re_path, include
from information import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$', views.main),
    re_path(r'(?P<slug>\w+)/(?P<sslug>\w+)/(?P<ssslug>\w*)/$', views.example),
    re_path(r'(?P<slug>\w+)/(?P<sslug>\w*)/$', views.construction),
    re_path(r'^contact/$', views.contactform),
    re_path(r'^thanks/$', views.thanks),
    re_path(r'(?P<slug>\w+)/$', views.main),

]
