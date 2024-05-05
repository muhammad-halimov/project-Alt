from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('competition/', views.competition, name='competition'),
    path('task/<str:pk>', views.task, name='task'),
    path('profile/', views.profile, name='profile'),
    path('monitor/<str:pk>/', views.monitor_unique, name='monitor_unique'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('codeforce/', views.codeforce, name='codeforce'),
    path('task_log/', views.task_log, name='task_log'),
]
