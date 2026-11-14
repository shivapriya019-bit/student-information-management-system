from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm


# Home Page
def home(request):
    return render(request, 'home.html')


# Add Student
@login_required
def student_input(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            return redirect('student_details', studentID=student.studentID)
        else:
            print(form.errors)
    else:
        form = StudentForm()

    return render(request, 'std_input.html', {'form': form})

# Update Student
@login_required
def student_update(request, studentID):
    std = get_object_or_404(Student, studentID=studentID)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=std)
        if form.is_valid():
            student = form.save()
            return redirect('student_details', studentID=student.studentID)
    else:
        form = StudentForm(instance=std)

    return render(request, 'std_update.html', {'form': form})


# Student Names List
@login_required
def student_names_list(request):
    students = Student.objects.all()
    return render(request, 'std_list.html', {'students': students})


# Student Details
@login_required
def student_details(request, studentID):
    student = get_object_or_404(Student, studentID=studentID)
    return render(request, 'std_details.html', {'student': student})


# Delete Student
@login_required
def student_delete(request, studentID):
    student = get_object_or_404(Student, studentID=studentID)

    if request.method == 'POST':
        student.delete()
        return redirect('home')

    return render(request, 'std_delete.html', {'student': student})