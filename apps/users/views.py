from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, models
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import models as tables
from .models import Vacations


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'users/login.html', {'title': 'Страница входа'})
    else:
        return render(request, 'users/login.html', {'title': 'Страница входа'})


def logout_user(request):
    logout(request)
    return render(request, 'users/login.html', {'title': 'Страница входа'})


@login_required
def profile(request):
    users = models.User.objects.get(username=request.user)
    context = {
        'firstname': users.first_name,
        'lastname': users.last_name,
        'email': users.email,
    }
    template = loader.get_template('users/profile.html')
    return HttpResponse(template.render(context, request))


@login_required
def vacation(request):
    return render(request, 'users/vacation.html')


@login_required
def add_vacation(request):
    if request.method == "POST":
        startdate = request.POST['startdate']
        finishdate = request.POST['finishdate']
        data = tables.Vacations(username=request.user, startdate=startdate, finishdate=finishdate, supervisor='На рассмотрении')
        data.save()
        return render(request, 'users/vacation.html')
    else:
        return render(request, 'users/vacation.html')

@login_required
def application(request):
    applications = Vacations.objects.filter(username=request.user.id).values()
    print(applications)

    return render(request, 'users/application.html', {'applications': applications})

