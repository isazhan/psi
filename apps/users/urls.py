from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('profile/', views.profile, name='profile'),
    path('profile/vacation/', views.vacation, name='vacation'),
    path('profile/vacation/addvacation/', views.add_vacation, name='add_vacation')
]