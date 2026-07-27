from .views import (home,student_input,student_update,student_names_list,student_details,student_delete)
from django.urls import path

urlpatterns=[
    path("",home,name="home"),
    path("input/",student_input,name="student_input"),
    path("update/<int:studentID>/",student_update,name="student_update"),
    path("list/",student_names_list,name="student_names_list"),
    path("details/<int:studentID>/",student_details,name="student_details"),
    path("delete/<int:studentID>/",student_delete,name="student_delete"),
]
