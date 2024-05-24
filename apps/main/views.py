from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from db import get_db_handle as db
from django.shortcuts import render, redirect


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


@login_required
def equipment_list(request, project_number):
    if request.method == 'POST':
        col = db()[project_number+'equipment_list']
        x = col.insert_one(request.POST.dict())
        return redirect('equipment_list', project_number)
    else:
        col = db()[project_number+'equipment_list']
        doc = col.find({})

        context = {
            'project_number': project_number,
            'equipment_list': doc,
        }
        
        template = loader.get_template('main/equipment_list.html')
        return HttpResponse(template.render(context, request))


@login_required
def equipment(request, project_number, equipment_tag):
    return