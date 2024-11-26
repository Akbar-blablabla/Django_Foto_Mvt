from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('courses/', views.course_list, name='course_list'),
    path('courses/<pk>/', views.course_detail, name='course_detail'),

    path('students/', views.student_list, name='student_list'),
    path('students/<pk>/', views.student_detail, name='student_detail'),

    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/<pk>/', views.teacher_detail, name='teacher_detail'),

    path('model_student/',views.model_student, name='model_student.'),
    path('model_course/', views.model_course, name='model_course.'),
    path('model_teacher/', views.model_teacher, name='model_teacher.'),
]
