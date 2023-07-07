from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import UserForm, RegisterForm, RegisterFormTeacher
from .models import Student, Teacher
from .data import predmet_all


def entrance(request):
    if request.method == "POST":
        username = request.POST.get("clas")
        password = request.POST.get("name")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if username in Student.objects.values_list('login', flat=True):
                return redirect('student/home')
            else:
                return redirect('teacher/home')
        else:
            try:
                Student.objects.get(login=username)
                return render(request, 'main/entrance.html', {'form': UserForm(), 'passw': True})
            except:
                return render(request, 'main/entrance.html', {'form': UserForm(), 'login': True})
    else:
        return render(request, "main/entrance.html", {"form": UserForm()})


def register(request):
    if request.method == 'POST':
        login = request.POST.get("login")
        password = request.POST.get("password")
        clas = request.POST.get("clas")
        name = request.POST.get("name")
        first_name = request.POST.get("first_name")
        image = request.FILES.get("image")
        if len(login) >= 5 and not (login in User.objects.values_list('username', flat=True)):
            user = User(username=login)
            user.set_password(password)
            user.save()
            Student(login=login, clas=clas, last_name=name, first_name=first_name, image=image).save()
            return redirect('entrance')
        else:
            if len(login) < 5:
                return render(request, 'main/register.html', {'form': RegisterForm(), 'short': True})
            else:
                return render(request, 'main/register.html', {'form': RegisterForm(), 'exists': True})
    else:
        return render(request, 'main/register.html', {'form': RegisterForm()})


def register_teacher(request):
    if request.method == 'POST':
        login = request.POST.get("login")
        password = request.POST.get("password")
        predmet = request.POST.get("predmet")
        name = request.POST.get("name")
        first_name = request.POST.get("first_name")
        pas_teach = request.POST.get("password_teacher")
        head_clas = request.POST.get("head_clas")
        image = request.FILES.get("image")

        if len(login) >= 5 and predmet in predmet_all and  not (login in User.objects.values_list('username', flat=True)) and pas_teach == "PaCDvZatwqg5":
            user = User(username=login)
            user.set_password(password)
            user.save()
            Teacher(login=login, last_name=name, first_name=first_name, predmet=predmet, head_clas=head_clas, image=image).save()
            return redirect('entrance')
        else:
            if len(login) < 5:
                return render(request, 'main/register_teacher.html', {'form': RegisterFormTeacher(), 'short': True})
            elif pas_teach != "PaCDvZatwqg5":
                return render(request, 'main/register_teacher.html', {'form': RegisterFormTeacher(), 'passw': True})
            elif pas_teach != "PaCDvZatwqg5":
                return render(request, 'main/register_teacher.html', {'form': RegisterFormTeacher(), 'predm': True})
            else:
                return render(request, 'main/register_teacher.html', {'form': RegisterFormTeacher(), 'login': True})
    else:
        return render(request, 'main/register_teacher.html', {'form': RegisterFormTeacher()})
