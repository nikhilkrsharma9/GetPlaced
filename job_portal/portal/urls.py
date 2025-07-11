from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'), # index or home page
    path('search', views.job_search, name='job_search'),  # the seach box in index.html or home page
    path('college_register', views.college_register, name='college_register'),
    path('college_login', views.college_login, name='college_login'),
    path('company_register', views.company_register, name='company_register'),
    path('company_login', views.company_login, name='company_login'),
    path('college_list', views.college_list, name='college_list'),
    path('company_list', views.company_list, name='company_list'),
    path('college_after_login/<int:college_id>/', views.college_after_login, name='college_after_login'),
    path('add_student/<int:college_id>/', views.add_student, name='add_student'),
    path('company_after_login/<int:company_id>/', views.company_after_login, name='company_after_login'),
    path('add_job/<int:company_id>/', views.add_job, name='add_job'),
    path('raise_ticket/', views.raise_ticket, name='raise_ticket'),
    path('chat_box/<int:ticket_id>/', views.chat_box, name='chat_box'),
    path('connect_ticket/<int:ticket_id>/<int:company_id>/', views.connect_ticket, name='connect_ticket'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)