from django.shortcuts import render
from django.http import HttpResponse 

def home(request):
    return render(request, 'index.html', {'name' : "STUDENT MANAGEMENT SYSTEM"})

def student(request):
    return render(request, 'student.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')