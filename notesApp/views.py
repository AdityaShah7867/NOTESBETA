from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from . models import UserAccount
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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

@login_required(login_url="/login/")
def notes(request):
    return render(request,'main/Topics.html')
@login_required(login_url="/login/")
def aut(request):

    return render(request,'main/autometa.html')

@login_required(login_url="/login/")
def math(request):
    return render(request,'main/Maths.html')

@login_required(login_url="/login/")
def pythont(request):
    return render(request,'main/pyhton.html')

@login_required(login_url="/login/")
def coa(request):
    return render(request,'main/Coa.html')

@login_required(login_url="/login/")
def cnnd(request):
    return render(request,'main/CNND.html')

@login_required(login_url="/login/")
def ost(request):
    return render(request,'main/OS.html')
    
@login_required(login_url="/login/")
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

def logoutT(request):
    logout(request)

    return redirect('login')

