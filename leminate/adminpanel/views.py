from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    if checkSessionVars(request):
        return render(request, 'adminpanel/index.html', {'request': request})
    return HttpResponseRedirect(reverse('login'))


def checkSessionVars(request):
    if 'userid' in request.session and 'is_admin' in request.session:
        if request.session['is_admin'] == 1:
            return True
    else:
        return False
