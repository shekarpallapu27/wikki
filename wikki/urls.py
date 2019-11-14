"""wikki URL Configuration

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
from wikkiapp.views import main,Wikki_Aricles,search_list_values
urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'download/$', Wikki_Aricles.download, name='download'),
    url(r'search_list/$', Wikki_Aricles.search_list, name='download'),
    url(r'search_list_values/$', search_list_values, name='download'),
]
