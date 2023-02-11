from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from . models import UserAccount
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request,'main/starter.html')

def loginH(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        userTyp = authenticate(email=email, password=password)

        if userTyp is not None:
            login(request, userTyp)
            return redirect('notes')
        else:
            return HttpResponse('Not Registered')




    return render(request,'authentication/LOGIN.HTML')

def notes(request):
    return render(request,'main/Topics.html')

def aut(request):

    return render(request,'main/autometa.html')

def math(request):
    return render(request,'main/Maths.html')

def pythont(request):
    return render(request,'main/pyhton.html')

def coa(request):
    return render(request,'main/Coa.html')

def cnnd(request):
    return render(request,'main/CNND.html')
def ost(request):
    return render(request,'main/OS.html')

def registerH(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = 'user'
        user = UserAccount.objects.create_user(email,name,password)
        user.save()

        return HttpResponse('okay')

    else:
        return render(request,'authentication/LOGIN.HTML')
