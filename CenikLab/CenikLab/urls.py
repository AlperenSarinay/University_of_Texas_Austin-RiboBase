"""CenikLab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('user/', include("user.urls")),
    path('AddExperiment/',views.AddExperiment,name="AddExperiment"),
    path('addData/',views.addData,name="addData"),
    path('DataSearch/',views.DataSearch,name="DataSearch"),
    path('DataDownload/',views.DataDownload,name="DataDownload"),
    path('DataSearchPage/<int:id>',views.DataSearchPage,name="DataSearchPage"),
    path('UpdateExperiment/<int:id>',views.UpdateExperiment,name="UpdateExperiment"),
    path('Comparasion/',views.Comparasion,name="Comparasion"),
    path('AddSRR/',views.AddSRR,name="AddSRR"),
    path('StudySearch/',views.StudySearch,name="StudySearch"),
    path('StudySearchPage/',views.StudySearchPage,name="StudySearchPage"),
    
]
