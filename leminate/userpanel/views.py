from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    if 'userid' in request.session and 'is_admin' in request.session:
        return render(request, 'userpanel/index.html')
    else:
        return HttpResponseRedirect(reverse('login'))
