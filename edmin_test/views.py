from datetime import date, datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from edmin_test.forms import CinemaForm, CinemaDeleteForm
from edmin_test.models import Cinema

def index(request):
    return render_to_response('index.html',
        {'cinemas': Cinema.objects.all()},
        context_instance=RequestContext(request))

def cinema_add(request):
    if request.method == "POST":
        form = CinemaForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('ajax/cinema_add_success.html',
                {},
                context_instance=RequestContext(request))
    else:
        form = CinemaForm()

    return render_to_response('ajax/cinema_add.html',
        {'form': form},
        context_instance=RequestContext(request))

def cinema_delete(request, cinema_id):
    if request.method == "POST":
        form = CinemaDeleteForm(request.POST)
        if form.is_valid():
            cinema = Cinema.objects.get(id=cinema_id)
            cinema.delete()
            return render_to_response('ajax/cinema_delete_success.html',
                {},
                context_instance=RequestContext(request))
        else:
            print form.errors
    return render_to_response('ajax/cinema_delete.html',
        {'cinema_id': cinema_id},
        context_instance=RequestContext(request))    

def cinema(request, cinema_id, presentations_date):
    cinema = get_object_or_404(Cinema, id=cinema_id)
    if not presentations_date:
        presentations_date = date.today()
    else:
        presentations_date = datetime.strptime(presentations_date, '%Y-%m-%d')
    next_day = presentations_date + timedelta(days=1)

    presentations = cinema.presentation_set.filter(
        time__gte = presentations_date, 
        time__lt = next_day)

    return render_to_response('cinema.html', {
            'cinema': cinema,
            'presentations_date': presentations_date.strftime('%Y-%m-%d'),
            'presentations': presentations
        },
        context_instance=RequestContext(request))  

def presentation_add(request, cinema_id, presentations_date):
    return HttpResponse('presentation dummy add %s %s' % (cinema_id, presentations_date))