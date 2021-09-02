from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_page, name='base_page'),
    path('success/<str:message>/', views.success, name='success'),
    path('trainers/', views.trainers_page, name='trainers_page'),
    path('trainer_add/', views.trainer_add, name='trainer_add'),
    path('trainer_edit/<int:id>/', views.trainer_edit, name='trainer_edit'),
    path('trainer_delete/<int:id>/', views.trainer_delete, name='trainer_delete'),
    path('trainer_details/<int:id>/', views.trainer_details, name='trainer_details'),
]
