from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from django.template import loader

@login_required
def index(request):
    projects = Projects.objects.all()

    context = {
        'projects': projects,
    }
    template = loader.get_template('main/index.html')




    return HttpResponse(template.render(context, request))