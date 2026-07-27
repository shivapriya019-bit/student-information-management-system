from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


# Home Page
def home(request):
    return render(request, 'home.html')


# Add Student
def student_input(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            return redirect('student_details', studentID=student.studentID)
    else:
        form = StudentForm()

    return render(request, 'std_input.html', {'form': form})


# Update Student
def student_update(request, studentID):
    std = Student.objects.get(studentID=studentID)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=std)
        if form.is_valid():
            student = form.save()
            return redirect('student_details', studentID=student.studentID)
    else:
        form = StudentForm(instance=std)

    return render(request, 'std_update.html', {'form': form})


# Student Names List
def student_names_list(request):
    students = Student.objects.all()
    return render(request, 'std_list.html', {'students': students})

# student Details
def student_details(request, studentID):
    student = Student.objects.get(studentID=studentID)
    return render(request, 'std_details.html', {'student': student})




# Delete Student
def student_delete(request, studentID):
    student =Student.objects.get( studentID=studentID)

    if request.method == 'POST':
        student.delete()
        return redirect('home')

    return render(request, 'std_delete.html', {'student': student})