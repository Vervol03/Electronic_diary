from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='teacher_home'),
    path('rozk', views.rozk, name='teacher_rozk'),
    path('estimates', views.estimates, name='teacher_estimates'),
    path('work', views.work, name='teacher_work')
]
