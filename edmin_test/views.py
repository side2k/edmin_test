from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from edmin_test.forms import CinemaForm

def index(request):
    return render_to_response('index.html',
        {},
        context_instance=RequestContext(request))

def cinema_add(request):
    if request.method == "POST":
        form = CinemaForm(request.POST)
    else:
        form = CinemaForm()

    return render_to_response('ajax/cinema_add.html',
        {'form': form},
        context_instance=RequestContext(request))
