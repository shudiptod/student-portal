from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout as logouts
from django.http import HttpResponse

from dashboard.models import Student,Course

# Create your views here


def loginpage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        else:
            return redirect("/login")
    context = {}
    return render(request, "registration/login.html", context)


def logoutPage(request):
    logouts(request)
    return redirect("login")


def dash(request):
    if request.user.is_authenticated:
        student = Student.objects.filter(user=request.user)
        if not student:
            return HttpResponse("student not found")
        student = student[0]

        context = {
            "student": student
        }

        return render(request, 'dashboard/dashboard.html', context)
    else:
        return redirect("/login")


def liveR(request):
    if request.user.is_authenticated:
        return render(request, 'LiveResult/Live Result.html')
    else:
        return redirect("/login")


def regcourse(request):
    if request.user.is_authenticated:
        course = Course.objects.filter(user=request.user)
        if not course:
            return HttpResponse("course not found")
        course = course[0]
        context = {
            "course": course
        }
        return render(request, 'RegCourse/registered.html', context)
    else:
        return redirect("/login")


def teEv(request):
    if request.user.is_authenticated:
        return render(request, 'TeachEval/TEvaluation.html')
    else:
        return redirect("/login")


def drop(request):
    if request.user.is_authenticated:
        return render(request, 'DropSeme/drop.html')
    else:
        return redirect("/login")


def ChangePass(request):
    if request.user.is_authenticated:
        return render(request, 'ChangePass/Password.html')
    else:
        return redirect("/login")
