from django.contrib import admin
from django.urls import path,include
from MoodLog.views import *

urlpatterns = [
    path('dashboard/',dashboard),
    path('create-moodlog/',create_moodlog),
    path('home/',home)
    
]