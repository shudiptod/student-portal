from django.shortcuts import render
# Create your views here

def dash(request):
    return render (request, 'dashboard/dashboard.html')

def liveR(request):
    return render (request, 'LiveResult/Live Result.html')

def regcourse(request):
    return render (request, 'RegCourse/Registered.html')

def teEv(request):
    return render (request, 'TeachEval/Teaching Evaluation.html')

def drop(request):
    return render (request, 'DropSeme/drop.html')

def ChangePass(request):
    return render (request,'ChangePass/Password.html')

  