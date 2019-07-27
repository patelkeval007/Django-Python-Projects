from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User
from django.conf import settings
from django.core.mail import send_mail
import math, random


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


def sendOTP(request):
    email = request.POST.get('email')
    if verify_email(email):
        subject = 'Leminates - Change PASS'
        otp = generateOTP()
        msg = 'OTP - ' + otp
        from_email = settings.EMAIL_HOST_USER
        to_list = ['']
        send_mail(subject, msg, from_email, to_list, fail_silently=False)
        return render(request, 'account/sendOTP.html', {'otp': otp, 'email': email})
    else:
        return HttpResponseRedirect(reverse('forgot_password'))


def verify_email(email):
    users = User.objects.all()
    for t_email in users:
        if t_email.email == email:
            return True
    return False


def generateOTP():
    # Declare a digits variable
    # which stores all digits
    digits = "0123456789"
    OTP = ""

    # length of password can be chaged
    # by changing value in range
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def change_password(request):
    otp = request.POST.get('otp')
    c_otp = request.POST.get('entered_otp')
    if (otp == c_otp):
        return render(request, 'account/change_password.html',{'email': request.POST.get('email')})
    else:
        return HttpResponseRedirect(reverse('forgot_password'))


def check_change_pass(request):
    p = request.POST.get('password')
    c_p = request.POST.get('c_password')
    email = request.POST.get('email')
    if c_p == p:
        print(email)
        User.objects.filter(email=email).update(password=p)
        return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponseRedirect(reverse('forgot_password'))
