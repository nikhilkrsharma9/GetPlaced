from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # index or home page
    path('search/', views.job_search, name='job_search'),  # the seach box in index.html or home page
]