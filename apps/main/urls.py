from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('access/', views.access, name='access'),
    path('projects/<int:project_id>/', views.project, name='project'),
    path('projects/<int:project_id>/equipment_list/', views.equipment_list, name='equipment_list'),
    path('projects/<int:project_id>/equipment_list/<str:equipment_tag>/', views.equipment, name='equipment'),
]