from django import forms
from .models import Categories


class CategoriesForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tur nomini kiriting'
    }), label='Tur nomi')
    definition = forms.CharField(max_length=300, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': "yangi tur haqida ma'lumot kiriting"
    }), label="Tur haqida ma'lumot")


class FlowerForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'gul nomini kiriting',
        'class': 'form-control'
    }), label='Gul nomi')
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': "gul haqida ma'lumot kiriting",
        'class': 'form-control'
    }), label='Gul haqida')
    price = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }), label='Gul narxi')
    published = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
        'checked': 'checked'
    }), label="Mavjud yoki yo'q")
    type = forms.ModelChoiceField(queryset=Categories.objects.all(), widget=forms.Select(attrs={
        'class': 'form-select'
    }), label="Bog'langan gul turi")
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        "placeholder": "gul nechtaligi",
        "class": "form-control"
    }))


class RegisterForm(forms.Form):
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
