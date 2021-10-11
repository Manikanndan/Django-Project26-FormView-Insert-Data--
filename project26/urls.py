"""project26 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic.base import TemplateView
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fbv_string/',fbv_string,name='fbv_string'),
    path('cbv_string/',cbv_string.as_view(),name='cbv_string'),
    path('fbv_html/',fbv_html,name='fbv_html'),
    path('cbv_html/',Cbv_html.as_view(),name='cbv_html'),
    path('fbv_form/',fbv_form,name='fbv_form'),
    path('cbv_form/',cbv_form.as_view(),name='cbv_form'),
    path('urltemp/',TemplateView.as_view(template_name='template.html'),name='urltemp'),
    path('Cbv_TemplateView/',Cbv_TemplateView.as_view(),name='Cbv_TemplateView'),
    path('Cbv_FormView/',Cbv_FormView.as_view(),name='Cbv_FormView'),
    path('CBVModel_FormView/',CBVModel_FormView.as_view(),name='CBVModel_FormView'),
    path('CBVModel_ListView/',CBVModel_ListView.as_view(),name='CBVModel_ListView'),
]
