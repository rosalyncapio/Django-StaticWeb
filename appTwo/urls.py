from django.urls import path
from . import views

urlpatterns = [
    path('project_list/', views.project_list, name='project_list'),
    path('project_detail/', views.project_detail, name='project_detail'),
    path('project_timeline/', views.project_timeline, name='project_timeline'),
]