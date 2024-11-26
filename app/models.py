from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course, related_name='students')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
