from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User


# Create your views here.
def index(request):
    return render(request, 'account/login.html')


def authenticateUser(request):
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
