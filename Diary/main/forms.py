from django import forms
from .data import CLASS_CHOICES

class UserForm(forms.Form):
    clas = forms.CharField(label="Логін")
    name = forms.CharField(label="Пароль")

class RegisterForm(forms.Form):
    login = forms.CharField(label="Логін")
    password = forms.CharField(label="Пароль")
    clas = forms.ChoiceField(label="Клас", choices=CLASS_CHOICES)
    name = forms.CharField(label="Ім'я")
    first_name = forms.CharField(label="Прізвище")
    image = forms.ImageField(label="Фото")

class RegisterFormTeacher(forms.Form):
    login = forms.CharField(label="Логін")
    password = forms.CharField(label="Пароль")
    predmet = forms.CharField(label="Предмети")
    name = forms.CharField(label="Ім'я")
    first_name = forms.CharField(label="Прізвище")
    password_teacher = forms.CharField(label="Пароль для вчителя")
    head_clas = forms.ChoiceField(label="Клас", choices=tuple([('Немає', 'Немає')]+list(CLASS_CHOICES)))
    image = forms.ImageField(label="Фото")
