from django.contrib import admin

from apps.task2.models import Vacancy


# Register your models here.

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'salary', 'published_date']