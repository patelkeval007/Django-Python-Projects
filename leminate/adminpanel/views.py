from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from account.models import User


def checkSessionVars(request):
    if 'id' in request.session and 'is_admin' in request.session:
        if request.session['is_admin'] == 1:
            return True
    else:
        return False


# Create your views here.
def index(request):
    if checkSessionVars(request):
        return render(request, 'adminpanel/index.html', {'request': request})
    return HttpResponseRedirect(reverse('login'))


def show_user(request):
    if checkSessionVars(request):
        users = User.objects.filter(is_admin=False)
        return render(request, 'adminpanel/show_user.html', {'users': users})


def update_user_page(request):
    if checkSessionVars(request):
        try:
            user = User.objects.filter(id=request.POST.get('id')).get()
            return render(request, 'adminpanel/update_user.html', {'user': user})
        except:
            return HttpResponseRedirect(reverse('show_user'))
    return HttpResponseRedirect(reverse('login'))


def update_user(request):
    # try:
    User.objects.filter(id=request.POST.get('id')).update(name=request.POST.get('name'),
                                                          email=request.POST.get('email'),
                                                          address=request.POST.get('address'),
                                                          dob=request.POST.get('dob'),
                                                          m_no=request.POST.get('m_no'))
    return HttpResponseRedirect(reverse('show_user'))


# except:
#     return HttpResponseRedirect(reverse('show_user'))


def del_user(request):
    if checkSessionVars(request):
        try:
            User.objects.get(id=request.POST.get('id')).delete()
            return HttpResponseRedirect(reverse('show_user'))
        except:
            return HttpResponseRedirect(reverse('show_user'))
