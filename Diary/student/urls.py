from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='student_home'),
    path('rozk', views.rozkl, name='student_rozk'),
    path('work', views.work, name='student_work')
]