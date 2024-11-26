from django.shortcuts import render
from .models import Teacher, Course, Student


def teacher_list(request):
    teacher = Teacher.objects.all()
    return render(request, 'app/teacher_list.html', {'teacher_list': teacher})


def teacher_detail(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    return render(request, 'app/teacher_detail.html', {'teacher': teacher})


def course_list(request):
    course = Course.objects.all()
    return render(request, 'app/course_list.html', {'course_list': course})


def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'app/course_detail.html', {'course': course})


def student_list(request):
    student = Student.objects.all()
    return render(request, 'app/student_list.html', {'student_list': student})


def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'app/student_detail.html', {'student': student})


def home(request):
    if request.method == 'GET':
        return render(request, 'app/home.html')


def model_student(request):
    if request.method == 'GET':
        return render(request, 'app/model_student.html')


def model_course(request):
    if request.method == 'GET':
        return render(request, 'app/model_course.html')


def model_teacher(request):
    if request.method == 'GET':
        return render(request, 'app/model_teacher.html')
