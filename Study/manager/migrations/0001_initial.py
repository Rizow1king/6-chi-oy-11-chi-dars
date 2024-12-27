# Generated by Django 5.1.4 on 2024-12-20 19:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nomi')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='course', verbose_name='Rasmi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Qoshilgan vaqti')),
                ('views', models.IntegerField(default=0, verbose_name="ko'rilgan soni")),
            ],
            options={
                'verbose_name': 'Kurs',
                'verbose_name_plural': 'Kurslar',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Darsni nomi')),
                ('teacher', models.CharField(max_length=100, verbose_name="O'qituvchi ismi")),
                ('theme', models.TextField(blank=True, default="Darsni mavzusi: qo'shilmagan", null=True, verbose_name='Darsni mavzusi')),
                ('homework', models.TextField(default='Darsni qatatdan korish va ozingiz uchun konspekt qiling', verbose_name='Uyga vazifa')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")),
                ('published', models.BooleanField(default=True, verbose_name='Bolganligi')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.course', verbose_name='Qaysi kursga boglangani')),
            ],
            options={
                'verbose_name': 'Dars',
                'verbose_name_plural': 'Darslar',
                'ordering': ['-id'],
            },
        ),
    ]