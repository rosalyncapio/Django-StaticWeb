from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def skills(request):
    return render(request, 'skills.html')

def contact(request):
    return render(request, 'contacts.html')
