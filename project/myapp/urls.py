from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>/', views.delete_feedback, name='delete'),
    path('edit/<int:id>/', views.edit_feedback, name='edit'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]