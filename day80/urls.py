"""day80 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login),
    url(r'^index/$', views.index),
    url(r'^userinfo/$', views.userinfo),
    url(r'^userinfo/add/$', views.userinfo_add),
    url(r'^userinfo/del/(\d+)/$', views.userinfo_del),
    url(r'^userinfo/edit/(\d+)/$', views.userinfo_edit),
    url(r'^order/$', views.order),
    url(r'^order/add/$', views.order_add),
    url(r'^order/del/(\d+)/$', views.order_del),
    url(r'^order/edit/(\d+)/$', views.order_edit),
]
