from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *


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
    users = CustomUser.objects.get(username=request.user)
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
        data = Vacations(username=request.user, startdate=startdate, finishdate=finishdate, supervisor='На рассмотрении')
        data.save()
        return render(request, 'users/vacation.html')
    else:
        return render(request, 'users/vacation.html')


@login_required
def application(request):
    applications = Vacations.objects.filter(username=request.user.id).values()
    return render(request, 'users/application.html', {'applications': applications})


@login_required
def sign_applications(request):
    # for supervisor
    vac_for_supervisor = Vacations.objects.select_related('username').filter(username__supervisor=request.user, supervisor = 'На рассмотрении')

    # for jun hr
    if request.user.position == 'jun_hr':
        vac_for_jun_hr = Vacations.objects.filter(jun_hr = 'На рассмотрении')
    else:
        vac_for_jun_hr = Vacations.objects.none()

    # for head hr
    if request.user.position == 'head_hr':
        vac_for_head_hr = Vacations.objects.filter(head_hr = 'На рассмотрении')
    else:
        vac_for_head_hr = Vacations.objects.none()

    # for director
    if request.user.position == 'director':
        vac_for_director = Vacations.objects.filter(director = 'На рассмотрении')
    else:
        vac_for_director = Vacations.objects.none()

    vacations = vac_for_supervisor | vac_for_jun_hr | vac_for_head_hr | vac_for_director

    context = {
        'vacations': vacations
    }
    template = loader.get_template('users/sign_applications.html')
    return HttpResponse(template.render(context, request))


@login_required
def accept_applications(request, applications_id):
    # sign as supervisor
    if Vacations.objects.select_related('username').get(id=applications_id).username.supervisor == str(request.user):
        x = Vacations.objects.get(id=applications_id)
        x.supervisor = 'Утверждено'
        x.jun_hr = 'На рассмотрении'
        x.save()

    # sign as jun hr
    if request.user.position == 'jun_hr':
        x = Vacations.objects.get(id=applications_id)
        x.jun_hr = 'Утверждено'
        x.head_hr = 'На рассмотрении'
        x.save()
    
    # sign as head hr
    if request.user.position == 'head_hr':
        x = Vacations.objects.get(id=applications_id)
        x.head_hr = 'Утверждено'
        x.director = 'На рассмотрении'
        x.save()
    
    # sign as director
    if request.user.position == 'director':
        x = Vacations.objects.get(id=applications_id)
        x.director = 'Утверждено'
        x.save()

    return redirect(sign_applications)


@login_required
def reject_applications(request):
    # reject as supervisor
    if Vacations.objects.select_related('username').get(id=request.POST['app-id']).username.supervisor == str(request.user):
        x = Vacations.objects.get(id=request.POST['app-id'])
        x.supervisor = 'Отклонено'
        x.comments = request.POST['comment']
        x.save()

    # reject as jun hr
    if request.user.position == 'jun_hr':
        x = Vacations.objects.get(id=request.POST['app-id'])
        x.jun_hr = 'Отклонено'
        x.comments = request.POST['comment']
        x.save()
    
    # reject as head hr
    if request.user.position == 'head_hr':
        x = Vacations.objects.get(id=request.POST['app-id'])
        x.head_hr = 'Отклонено'
        x.comments = request.POST['comment']
        x.save()
    
    # reject as director
    if request.user.position == 'director':
        x = Vacations.objects.get(id=request.POST['app-id'])
        x.director = 'Отклонено'
        x.comments = request.POST['comment']
        x.save()

    return redirect(sign_applications)

@login_required
def all_applications(request):
    if request.user.position == 'jun_hr' or request.user.position == 'head_hr':
        all_applications = Vacations.objects.all()
    else:
        all_applications = None
    return render(request, 'users/all_applications.html', {'all_applications': all_applications})

@login_required
def delete_application(request):
    if Vacations.objects.get(id=application.id).username == request.user:
        application.delete()
    return redirect(application)