from django.shortcuts import render, redirect
from student.models import Work, Rozk, Estimates
from main.models import Teacher, Student
from .data import all_class, clas_id, login

def home(request):
    try:
        teacher = Teacher.objects.get(login=request.user)
        teacher.image = str(teacher.image).split("/")[-1]
        return render(request, "teacher/home.html", {'data': teacher, 'head_clas':teacher.head_clas})
    except:
        return redirect('entrance')


def rozk(request):
    try:
        if request.method == "POST":
            teacher = Teacher.objects.get(login=request.user)
            rozklad = Rozk.objects.get(clas=teacher.head_clas)
            day = request.POST.get("day")
            days = day.split('\r\n')
            for i in days:
                if i not in all_class[teacher.head_clas.split('-')[0]]:
                    rozklad_len = {}
                    rozklad_len['Monday'] = len(rozklad.Monday.split('\r\n'))
                    rozklad_len['Tuesday'] = len(rozklad.Tuesday.split('\r\n'))
                    rozklad_len['Wednesday'] = len(rozklad.Wednesday.split('\r\n'))
                    rozklad_len['Thursday'] = len(rozklad.Thursday.split('\r\n'))
                    rozklad_len['Friday'] = len(rozklad.Friday.split('\r\n'))
                    return render(request, "teacher/rozk.html", {'rozklad': rozklad,
                                                                 'predmet':i,
                                                                 'rozklad_len':rozklad_len,
                                                                 'check':True,
                                                                 'head_clas': teacher.head_clas})
            if "Monday"    in request.POST: rozklad.Monday = day
            if "Tuesday"   in request.POST: rozklad.Tuesday = day
            if "Wednesday" in request.POST: rozklad.Wednesday = day
            if "Thursday"  in request.POST: rozklad.Thursday = day
            if "Friday"    in request.POST: rozklad.Friday = day
            rozklad.save()
            return redirect('teacher_rozk')
        else:
            teacher = Teacher.objects.get(login=request.user)
            rozklad = Rozk.objects.get(clas=teacher.head_clas)
            rozklad_len = {}
            rozklad_len['Monday'] = len(rozklad.Monday.split('\r\n'))
            rozklad_len['Tuesday'] = len(rozklad.Tuesday.split('\r\n'))
            rozklad_len['Wednesday'] = len(rozklad.Wednesday.split('\r\n'))
            rozklad_len['Thursday'] = len(rozklad.Thursday.split('\r\n'))
            rozklad_len['Friday'] = len(rozklad.Friday.split('\r\n'))
            return render(request, "teacher/rozk.html", {'rozklad': rozklad,
                                                         'rozklad_len':rozklad_len,
                                                         'head_clas':teacher.head_clas})
    except:
        return redirect('entrance')


def estimates(request):
    teacher = Teacher.objects.get(login=request.user)
    teacher.image = str(teacher.image).split("/")[-1]
    if request.method == "POST":
        for i in Student.objects.all():
            if i.clas in request.POST:
                clas_id[request.user.id] = i.clas
                students = {j.login: [j.last_name, j.first_name] for j in Student.objects.filter(clas=i.clas)}
                return render(request, "teacher/estimates_clas.html", {'students': dict(sorted(students.items())),
                                                                        'head_clas': teacher.head_clas,'clas':i.clas})
            for i in Student.objects.all():
                if i.login in request.POST:
                    student = Student.objects.get(login=i.login)
                    try:
                        login[request.user.id] = i.login
                        estimates = {j.predmet: j.estimate for j in Estimates.objects.filter(login=student.id)}
                        estimates = {j: '' if j not in estimates.keys() else estimates[j] for j in all_class[student.clas.split('-')[0]]}
                    except:
                        estimates = {}
                        estimates = {j: '' if j not in estimates.keys() else estimates[j] for j in all_class[student.clas.split('-')[0]]}
                    return render(request, "teacher/estimates_student.html", {'estimates': dict(sorted(estimates.items())),
                                                                              'head_clas':teacher.head_clas,
                                                                              'first':i.first_name, 'last':i.last_name})

        for i in all_class[clas_id[request.user.id].split('-')[0]]:
            if i in request.POST:
                student = Student.objects.get(login=login[request.user.id])
                estimate = request.POST.get("estimate").replace(",", " ").replace(" ", ",").split(",")
                estimate = ", ".join([num for num in estimate if num.isdigit() and 0 < int(num) < 13])
                if not Estimates.objects.filter(login=student.id, predmet=i):
                    Estimates(login=student, predmet=i, estimate=estimate).save()
                else:
                    estimates = Estimates.objects.get(login=student.id, predmet=i)
                    estimates.estimate = estimate
                    estimates.save()
                    break

        student = Student.objects.get(login=login[request.user.id])
        try:
            estimates = {i.predmet: i.estimate for i in Estimates.objects.filter(login=student.id)}
            estimates = {i: '' if i not in estimates.keys() else estimates[i] for i in all_class[student.clas.split('-')[0]]}
        except:
            estimates = {i: '' for i in all_class[student.clas.split('-')[0]]}
        return render(request, "teacher/estimates_student.html", {'estimates': dict(sorted(estimates.items())),
                                                                  'head_clas':teacher.head_clas,
                                                                  'first':student.first_name,'last':student.last_name})

    else:
        classes = []
        for i in Student.objects.all():
            if i.clas not in classes: classes.append(i.clas)
        return render(request, "teacher/estimates.html", {'classes': sorted(classes),
                                                          'head_clas':teacher.head_clas})


def work(request):
    teacher = Teacher.objects.get(login=request.user)
    teacher.image = str(teacher.image).split("/")[-1]
    try:
        if request.method == "POST":
            for i in Student.objects.all():
                if i.clas in request.POST:
                    clas_id[request.user.id] = i.clas
                    works = {j.predmet: j.work for j in Work.objects.filter(clas=i.clas)}
                    works = {j: '' if j not in works.keys() else works[j] for j in all_class[i.clas.split('-')[0]]}
                    return render(request, "teacher/work_class.html", {'works': dict(sorted(works.items())),
                                                                       'clas': i.clas,
                                                                       'head_clas':teacher.head_clas})

            for i in all_class[clas_id[request.user.id].split('-')[0]]:
                if i in request.POST:
                    if not Work.objects.filter(clas=clas_id[request.user.id], predmet=i):
                        Work(clas=clas_id[request.user.id], predmet=i, work=request.POST.get("work")).save()
                    else:
                        works = Work.objects.get(clas=clas_id[request.user.id], predmet=i)
                        works.work = request.POST.get("work")
                        works.save()
                        break

            works = {j.predmet: j.work for j in Work.objects.filter(clas=clas_id[request.user.id])}
            works = {j: '' if j not in works.keys() else works[j] for j in all_class[clas_id[request.user.id].split('-')[0]]}
            return render(request, "teacher/work_class.html", {'works': dict(sorted(works.items())),
                                                               'clas':clas_id[request.user.id],
                                                               'head_clas':teacher.head_clas})
        else:
            student = Student.objects.all()
            classes = []
            for i in student:
                if i.clas not in classes: classes.append(i.clas)
            return render(request, "teacher/work.html", {'classes': sorted(classes), 'head_clas':teacher.head_clas})
    except:
        return redirect('entrance')