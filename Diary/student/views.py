from django.shortcuts import render, redirect
from .models import Rozk, Work, Estimates
from main.models import Student
from .data import all_class


def home(request):
    try:
        student = Student.objects.get(login=request.user)
        student.image = str(student.image).split("/")[-1]
        estimates = {i.predmet: [int(j) if j != '' else 0 for j in i.estimate.split(', ')] for i in Estimates.objects.filter(login=student.id)}
        estimates = {i: [0] if i not in estimates.keys() else estimates[i] for i in all_class[student.clas.split('-')[0]]}
        estimates_student = {key: 0 if el==[0] else sum(el)/len(el) for key, el in estimates.items()}
        result_rating = {i: len(Student.objects.filter(clas=student.clas)) for i in all_class[student.clas.split('-')[0]]}
        for stud in Student.objects.filter(clas=student.clas):
            estimates_clas = {i.predmet: [int(j) if j != '' else 0 for j in i.estimate.split(', ')] for i in Estimates.objects.filter(login=stud.id)}
            estimates_clas = {i: [0] if i not in estimates_clas.keys() else estimates_clas[i] for i in all_class[stud.clas.split('-')[0]]}
            estimates_clas_rating = {key: 0 if el==[0] else sum(el)/len(el) for key, el in estimates_clas.items()}
            for j in all_class[student.clas.split('-')[0]]: result_rating[j] -= 1 if estimates_clas_rating[j] < estimates_student[j] else 0
        maxim = max([len(el) for _, el in estimates.items()])
        estimates = {key: ['']*maxim+['-'] if el==[0] else el+['']*(maxim-len(el))+['№'+str(result_rating[key])] for key, el in estimates.items()}
        return render(request, "student/home.html", {'data': student, 'estimates': dict(sorted(estimates.items())), 'max': maxim})
    except:
        return redirect('entrance')

def rozkl(request):
    try:
        student = Student.objects.get(login=request.user)
        rozk = Rozk.objects.get(clas=student.clas)
        time = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"]
        item = [('Monday', 'lenMonday', rozk.Monday),
                ('Tuesday', 'lenTuesday', rozk.Tuesday),
                ('Wednesday', 'lenWednesday', rozk.Wednesday),
                ('Thursday', 'lenThursday', rozk.Thursday),
                ('Friday', 'lenFriday', rozk.Friday)]
        rozk = {}
        for i in item:
            rozk[i[0]] = i[2].split('\r\n')
            rozk[i[1]] = str(len(rozk[i[0]]) + 1)
            rozk[i[0]] = dict(zip(time[:int(rozk[i[1]])], rozk[i[0]]))
        return render(request, "student/rozk.html", {'rozk': rozk, 'class': student.clas})
    except:
        return redirect('entrance')

def work(request):
    try:
        student = Student.objects.get(login=request.user)
        works = {i.predmet: i.work for i in Work.objects.filter(clas=student.clas)}
        works = {i: '' if i not in works.keys() else works[i] for i in all_class[student.clas.split('-')[0]]}
        return render(request, "student/work.html", {'works': dict(sorted(works.items())), 'clas':student.clas})
    except:
        return redirect('entrance')
