from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'studentID',
        'name',
        'Age',
        'gender',
        'Email',
        'phonenumber',
        'course',
        'DOJ',
    )

    search_fields = (
        'studentID',
        'name',
        'Email',
        'phonenumber',
    )

    list_filter = (
        'gender',
        'course',
        'DOJ',
    )