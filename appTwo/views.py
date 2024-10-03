
from django.shortcuts import render

def project_list(request):
    return render(request, 'project_list.html')

def project_detail(request):
    return render(request, 'project_detail.html')

def project_timeline(request):
    return render(request, 'project_timeline.html')