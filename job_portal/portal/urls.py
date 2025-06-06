from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('search/', views.job_search, name='job_search'),
]