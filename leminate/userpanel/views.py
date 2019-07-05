from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    if checkSessionVars(request):
        return render(request, 'userpanel/index.html')
    return HttpResponseRedirect(reverse('login'))


def contact(request):
    if checkSessionVars(request):
        return render(request, 'userpanel/contact.html')
    return HttpResponseRedirect(reverse('login'))


def about(request):
    if checkSessionVars(request):
        return render(request, 'userpanel/about.html')
    return HttpResponseRedirect(reverse('login'))


def checkSessionVars(request):
    if 'userid' in request.session and 'is_admin' in request.session:
        if request.session['is_admin'] == 0:
            return True
    else:
        return False
