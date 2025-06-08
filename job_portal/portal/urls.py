from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # index or home page
    path('search', views.job_search, name='job_search'),  # the seach box in index.html or home page
    path('college_register', views.college_register, name='college_register'),
    path('college_login', views.college_login, name='college_login'),
    path('company_register', views.company_register, name='company_register'),
    path('company_login', views.company_login, name='company_login'),
]