from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User


# Create your views here.
def index(request):
    return checkSessionVars(request)


def checkSessionVars(request):
    if 'id' in request.session and 'is_admin' in request.session:
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
        id = object.id
        name = object.name
        email = object.email
        password = object.password
        isAdmin = object.is_admin
    except:
        id, email, password, isAdmin, name = None, None, None, None, None

    if id is None or email is None or password is None or isAdmin is None or name is None:
        return render(request, 'account/login.html')
    else:
        request.session['id'] = id
        request.session['name'] = name
        request.session['email'] = email
        request.session['is_admin'] = isAdmin
        print(isAdmin)
        if isAdmin == 1:
            return HttpResponseRedirect(reverse('adminpanel'))
        elif isAdmin == 0:
            return HttpResponseRedirect(reverse('userpanel'))
        else:
            return HttpResponseRedirect(reverse('login'))


def logout(request):
    try:
        del request.session['id']
        del request.session['is_admin']
        request.session.flush()
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('login'))


def register(request):
    return render(request, 'account/register.html')


def authenticateUserRegistration(request):
    tName = request.POST.get('name')
    tEmail = request.POST.get('email')
    tAddress = request.POST.get('address')
    tdob = request.POST.get('dob')
    tm_no = request.POST.get('m_no')
    tPassword = request.POST.get('password')
    tCPassword = request.POST.get('c_password')

    if tName is "" or tEmail is "" or tPassword is "" or tCPassword is "" or tAddress is "" or tdob is "" or tm_no is "":
        return HttpResponseRedirect(reverse('register'))
    elif tPassword != tCPassword:
        return HttpResponseRedirect(reverse('register'))
    else:
        try:
            User.objects.filter(email=tEmail).get()
            return HttpResponseRedirect(reverse('register'))
        except:
            putData = User(name=tName, email=tEmail, address=tAddress, dob=tdob, m_no=tm_no, password=tPassword)
            putData.save()
    return HttpResponseRedirect(reverse('login'))


def forgotPassword(request):
    return render(request, 'account/forgot-password.html')
