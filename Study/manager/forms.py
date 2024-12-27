from django import forms
from .models import Course


class CourseForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'kurs nomini kiriting!',
        'class': "form-control"

    }), label="Dars nomi")

    photo = forms.ImageField(widget=forms.FileInput(attrs={
        "class": 'form-control'
    }), label='Rasmi', required=False)


class LessonForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=10, widget=forms.TextInput(attrs={
        "placeholder": "darsni nomini kiriting",
        "class": "form-control"
    }), label='Darsni nomi')
    teacher = forms.CharField(max_length=100, min_length=10, widget=forms.TextInput(attrs={
        "placeholder": "O'qituvchini ismini kiriting",
        "class": "form-control"
    }), label="O'qituvchini ismi")
    theme = forms.CharField(max_length=100, min_length=10, widget=forms.Textarea(attrs={
        "placeholder": "darsni mavzusini kiriting",
        "class": "form-control"
    }), label="Darsni mavzusi")
    homework = forms.CharField(max_length=100, min_length=10, widget=forms.Textarea(attrs={
        "placeholder": "uyga vazifani kiriting",
        "class": "form-control",
        "value": "Darsni qaytadan ko‘ring va o‘zingiz uchun konspekt qiling"
    }), label="Uyga vazifa")

    published = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': "form-check-input",
        'checked': 'checked'
    }), label='Saytda korinishi')
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={
        'class': 'form-select'
    }), label="Bog'langan kursi")
    student_count = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': "Talabalar sonini kiriting",
        'class': 'form-control'
    }), label='Talabalar soni')
    photo = forms.ImageField(widget=forms.FileInput(attrs={
        "class": 'form-control'
    }), label='Rasmi', required=False)


class Registerform(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        "class": 'form-control form-control-lg',
        "placeholder": 'Ismingizni kiriting'
    }), label='Ism:')

    email = forms.EmailField(max_lenth=100, widget=forms.EmailInput(attrs={
        "class": "form-control form-control-lg",
        "placeholder": "Elektron pochta manzilini kiriting:"
    }), label='Elektron pochta manzilli')

    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        "class": "form-control form-control-lg",
        "placeholder": "Parolingizni kirting:"
    }), label="Parol:")

    password_repeat = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        "class": "form-control form-control-lg",
        "placeholder": "Parolingizni qaytatdan kirting:"
    }), label="Parolni tasdiqlash:")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        "class": 'form-control form-control-lg',
        "placeholder": 'Ismingizni kiriting'
    }), label='Ism:')

    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        "class": "form-control form-control-lg",
        "placeholder": "Parolingizni kirting:"
    }), label="Parol:")
