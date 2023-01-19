from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, models
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


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