from django.shortcuts import render,HttpResponse
from .models import Project,Service



# Create your views here.
def portfolio(request):
    projects = Project.objects.all() 
    services = Service.objects.all()
    return render(request, "portfolio/portfolio.html", 
        {
        'projects':projects,
        'services':services})

