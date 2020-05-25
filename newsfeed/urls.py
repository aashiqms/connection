from django.contrib import admin
from django.urls import path, include
from . views import HomePageTemplateView

urlpatterns = [
    path('home/', HomePageTemplateView.as_view(), name='homepage_template_view'),


]
