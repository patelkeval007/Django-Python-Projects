from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User


# Create your views here.
def index(request):
    return checkSessionVars(request)


def checkSessionVars(request):
    if 'userid' in request.session and 'is_admin' in request.session:
        if request.session['is_admin'] == 0:
            return HttpResponseRedirect(reverse('userpanel'))
        elif request.session['is_admin'] == 1:
            return HttpResponseRedirect(reverse('adminpanel'))
    else:
        return render(request, 'account/login.html')


def authenticateUserLogin(request):
    tEmail = request.POST.get('email')
    tPassword = request.POST.get('password')
    try:
        object = User.objects.filter(email=tEmail, password=tPassword).get()
        email = object.email
        id = object.id
        password = object.password
        isAdmin = object.is_admin
    except:
        id, email, password, isAdmin = None, None, None, None

    if id is None or email is None or password is None or isAdmin is None:
        return render(request, 'account/login.html')
    else:
        request.session['userid'] = id
        request.session['email'] = email
        request.session['is_admin'] = isAdmin
        if isAdmin == 1:
            return HttpResponseRedirect(reverse('adminpanel'))
        elif isAdmin == 0:
            return HttpResponseRedirect(reverse('userpanel'))
        else:
            return HttpResponseRedirect(reverse('login'))


def logout(request):
    try:
        del request.session['userid']
        del request.session['is_admin']
        request.session.flush()
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('login'))


def register(request):
    return render(request, 'account/register.html')


def authenticateUserRegistration(request):
    tFname = request.POST.get('fname')
    tLname = request.POST.get('lname')
    tEmail = request.POST.get('email')
    tPassword = request.POST.get('password')
    tCPassword = request.POST.get('c_password')

    if tFname is "" or tLname is "" or tEmail is "" or tPassword is "" or tCPassword is "":
        return HttpResponseRedirect(reverse('register'))
    elif tPassword != tCPassword:
        return HttpResponseRedirect(reverse('register'))
    else:
        putData = User(firstname=tFname, lastname=tLname, email=tEmail, password=tPassword)
        putData.save()
    return HttpResponseRedirect(reverse('login'))


def forgotPassword(request):
    return render(request, 'account/forgot-password.html')
