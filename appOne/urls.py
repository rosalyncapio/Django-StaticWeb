from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('contacts/', views.contact, name='contacts'),
    

]