from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/<str:project_number>/', views.project, name='project'),
    path('projects/<str:project_number>/equipment_list/', views.equipment_list, name='equipment_list'),
    path('projects/<str:project_number>/equipment_list/<str:equipment_tag>/', views.equipment, name='equipment'),
]