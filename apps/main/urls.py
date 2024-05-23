from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/<str:project_number>/', views.project, name='project')
]