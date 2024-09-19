from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from db import get_db_handle as db
from django.shortcuts import render, redirect


@login_required
def index(request):
    if request.method == 'POST':
        data = request.POST.dict()
        col = db()['projects']

        doc = col.find({}, {'_id': 0, 'project_id': 1}).sort('_id', -1).limit(1)
        try:
            project_id = doc[0]['project_id'] + 1
        except:
            project_id = 100000
        
        data['project_id'] = project_id

        x = col.insert_one(data)
        
    col = db()['projects']
    doc = col.find({})

    context = {
        'projects': doc
    }

    template = loader.get_template('main/index.html')

    return HttpResponse(template.render(context, request))


@login_required
def access(request):
    if request.user.email == 'u.isazhan@psi-group.kz':
        if request.method == 'POST':
            col = db()['access']
        else:
            col = db()['access']
            doc = col.find({})
            context = {
                'access': doc
            }
            template = loader.get_template('main/access.html')
            return HttpResponse(template.render(context, request))
    else:
        return redirect('index')



@login_required
def project(request, project_id):
    col = db()['projects']
    doc = col.find_one({'project_id': project_id})

    context = {
        'project_id': project_id,
        'project_number': doc['project_number'],
        'project_name': doc['project_name'],
    }
    
    template = loader.get_template('main/project.html')
    return HttpResponse(template.render(context, request))


@login_required
def equipment_list(request, project_id):
    if request.method == 'POST':
        col = db()[str(project_id)+'equipment_list']
        x = col.insert_one(request.POST.dict())
        return redirect('equipment_list', project_id)
    else:
        col = db()[str(project_id)+'equipment_list']
        equipment_list = col.find({})
        equipment_tags = col.find({}, {"_id": 0, "equipment_tag": 1})

        context = {
            'project_id': project_id,
            'project_number': db()['projects'].find_one({'project_id': project_id})['project_number'],
            'project_name': db()['projects'].find_one({'project_id': project_id})['project_name'],
            'equipment_list': equipment_list,
            'equipment_tags': equipment_tags,
        }
        
        template = loader.get_template('main/equipment_list.html')
        return HttpResponse(template.render(context, request))


@login_required
def equipment(request, project_id, equipment_tag):
    if request.method == 'POST':
        col = db()[str(project_id)+'equipment_list']
        query = {'equipment_tag': equipment_tag}
        value = {'$set': request.POST.dict()}
        x = col.update_one(query, value)
        return redirect('equipment_list', project_id)
    else:
        col = db()[str(project_id)+'equipment_list']
        query = {'equipment_tag': equipment_tag}
        doc = col.find_one(query)

        context = {
            'project_id': project_id,
            'project_number': db()['projects'].find_one({'project_id': project_id})['project_number'],
            'project_name': db()['projects'].find_one({'project_id': project_id})['project_name'],
            'equipment': doc,
        }

        template = loader.get_template('main/equipment.html')
        return HttpResponse(template.render(context, request))