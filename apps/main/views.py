from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from django.template import loader
from db import get_db_handle as db

@login_required
def index(request):
    if request.method == 'POST':
        col = db()['projects']
        x = col.insert_one(request.POST.dict())
        
    col = db()['projects']
    doc = col.find({})

    context = {
        'projects': doc
    }

    template = loader.get_template('main/index.html')

    return HttpResponse(template.render(context, request))

@login_required
def project(request, project_number):

    context = {
        'project_number': project_number
    }
    
    template = loader.get_template('main/project.html')
    return HttpResponse(template.render(context, request))