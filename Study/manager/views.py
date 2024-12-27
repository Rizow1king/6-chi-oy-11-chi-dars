from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def home(request: WSGIRequest):
    lessons = Lesson.objects.all()
    context = {
        "lessons": lessons,
        'title': 'Barcha kurs hamda darslar'
    }
    return render(request, "index.html", context)


def lessons_by_courses(request: WSGIRequest, course_id):
    course = get_object_or_404(Course, id=course_id)
    lesson = Lesson.objects.filter(course_id=course_id)

    context = {
        'courses': [course],
        'lessons': lesson,
    }

    return render(request, 'index.html', context)


def lessons(request: WSGIRequest, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    context = {
        'lesson': lesson,
        'title': f'{lesson.name} - batafsil ma\'lumot'
    }
    return render(request, 'detail.html', context)


def course(request: WSGIRequest, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    course = get_object_or_404(Course, id=lesson.course.id)
    course.views += 1
    course.save()
    context = {
        'lesson': lesson,
        'title': lesson.description
    }

    return render(request, 'detail.html', context)


def add_course(request: WSGIRequest):
    if request.method == 'POST':
        form = CourseForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            course = Course.objects.create(**form.cleaned_data)
            print(course, "qo'shildi!")
            return redirect('home')
    else:
        form = CourseForm()

    context = {
        "form": form
    }
    return render(request, 'add_course.html', context)


def add_lesson(request: WSGIRequest):
    if request.method == 'POST':
        form = LessonForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            lesson = Lesson.objects.create(**form.cleaned_data)
            print(lesson, "qo'shildi!")
            messages.success(request, "Dars muvaffaqiyatli tarzda qo'shildi")
            return redirect('detail_lesson', lesson_id=lesson.pk)
    else:
        form = LessonForm()

    context = {
        "form": form
    }
    return render(request, 'add_lesson.html', context)


def update_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == 'POST':
        form = LessonForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            lesson.name = form.cleaned_data.get('name')
            lesson.teacher = form.cleaned_data.get('teacher')
            lesson.theme = form.cleaned_data.get('theme')
            lesson.homework = form.cleaned_data.get('homework')
            lesson.photo = form.cleaned_data.get('photo') if form.cleaned_data.get('photo') else lesson.photo
            lesson.student_count = form.cleaned_data.get('student_count')
            lesson.published = form.cleaned_data.get('published')
            lesson.course = form.cleaned_data.get('course')
            lesson.save()
            messages.success(request, "Dars muvaffaqiyatli tarzda o'zgartirildi!")
            return redirect('detail_lesson', lesson_id=lesson.pk)
    form = LessonForm(initial={
        'name': lesson.name,
        'teacher': lesson.teacher,
        'theme': lesson.theme,
        'homework': lesson.homework,
        'student_count': lesson.student_count,
        'published': lesson.published,
        'course': lesson.course,
        "photo": lesson.photo
    })
    context = {
        'form': form,
        'photo': lesson.photo,
    }
    return render(request, 'detail.html', context)


def delete_lesson(request, lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)
    course_id = lesson.course.id
    if request.method == 'POST':
        lesson.delete()
        messages.success(request, "Dars muvaffaqiyatli tarzda o'chirildi!")
        return redirect('course', course_id=course_id)
    context = {
        'lesson': lesson
    }
    messages.warning(request, "Ushbu darsni o'chirmoqchimisiz?")
    return render(request, 'confirm_delete.html', context)


def register(request):
    if request.method == "POST":
        form = Registerform(data=request.POST)
        if form.is_valid():
            password = form.cleaned_dats.get("password")
            password_repeat = form.cleaned_dats.get("password_repeat")
            if password_repeat == password:
                user = User.objects.create_user(
                    form.cleaned_data.get("username"),
                    form.cleaned_data.get("email"),
                    password
                )
                messages.success(request, "Akkaunt qoshildi!!")
                return redirect('home')
    context = {
        "forms": Registerform()
    }
    return render(request, "auth/register.html", context)


def login_user(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid:
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            messages.success(request, "Saytimizga xush kelibsiz")
            login(request, user)
            return redirect('home')

    context = {
        "forms": LoginForm()
    }
    return render(request, "auth/login.html", context)


def logoutPage(request: WSGIRequest):
    logout(request)
    messages.success(request, "Tizimdan muvaffaqiyatli chiqdingiz!")
    return redirect('home')
