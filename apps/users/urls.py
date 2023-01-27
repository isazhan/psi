from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('profile/', views.profile, name='profile'),
    path('profile/vacation/', views.vacation, name='vacation'),
    path('profile/vacation/addvacation/', views.add_vacation, name='add_vacation'),
    path('profile/application/', views.application, name='application'),
    path('sign_applications/', views.sign_applications, name='sign_applications'),
    path('accept_applications/', views.accept_applications, name='accept_applications'),
]