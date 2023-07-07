from django.urls import path
from . import views

urlpatterns = [
    path('',     views.entrance, name='entrance'),
    path('register', views.register, name='register'),
    #path('кінець url-адресу', функція яка обродляє його, ім'я для посилання)
    path('register_teacher', views.register_teacher, name='register_teacher')
]
