from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_list(request):
    return render(request, 'projects/index.html')
    # return HttpResponse("<h1>Hello Raps Fan!</h1>")
    # return none if nothing returned!
    # Can input html strings to display for the view!

def all_projects(request):
    # query database to return all projects objects
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html', {'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/detail.html', {'project': project})
