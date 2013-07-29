from datetime import date, datetime, timedelta

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson

from edmin_test.forms import CinemaForm, ConfirmationForm, PresentationForm
from edmin_test.models import Cinema, Presentation

def index(request):
    return render_to_response('index.html',
        {'cinemas': Cinema.objects.all()},
        context_instance=RequestContext(request))

def _json_response(data):
    return HttpResponse(simplejson.dumps(data), content_type='application/json')

def _success(data=None):
    result = {}
    if data and type(data) == dict:
        result.update(data)
    result['success'] = True
    return _json_response(result)

def _form_errors(form):
    result = {'errors':form.errors}
    result['success'] = False;
    return _json_response(result)

def cinema_add(request):
    if request.method == "POST":
        form = CinemaForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return _success({'id': instance.id})
        else:
            return _form_errors(form)
    raise PermissionDenied

def cinema_edit(request, cinema_id):
    cinema = get_object_or_404(Cinema, id=cinema_id)
    if request.method == "POST":
        form = CinemaForm(request.POST, instance=cinema)
        if form.is_valid():
            form.save()
            return render_to_response('ajax/cinema_edit_success.html',
                {},
                context_instance=RequestContext(request))    
    else:
        form = CinemaForm(instance=cinema)

    return render_to_response('ajax/cinema_edit.html',
        {'form': form},
        context_instance=RequestContext(request))

def cinema_delete(request, cinema_id):
    if request.method == "POST":
        form = ConfirmationForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirmed']:
            cinema = Cinema.objects.get(id=cinema_id)
            cinema.delete()
            return render_to_response('ajax/cinema_delete_success.html',
                {},
                context_instance=RequestContext(request))
        else:
            raise Exception("Form contains errors: %s" % form.errors)
    return render_to_response('ajax/cinema_delete.html',
        {'cinema_id': cinema_id},
        context_instance=RequestContext(request))    

def _get_presentations_date(presentations_date):
    if not presentations_date:
        return date.today()
    else:
        return datetime.strptime(presentations_date, settings.DATE_FORMAT)

def cinema(request, cinema_id, presentations_date):
    cinema = get_object_or_404(Cinema, id=cinema_id)
    presentations_date = _get_presentations_date(presentations_date)
    next_day = presentations_date + timedelta(days=1)

    presentations = cinema.presentation_set.filter(
        time__gte = presentations_date, 
        time__lt = next_day)

    return render_to_response('cinema.html', {
            'cinema': cinema,
            'presentations_date': presentations_date.strftime(settings.DATE_FORMAT),
            'presentations': presentations
        },
        context_instance=RequestContext(request))  

def presentation_add(request, cinema_id, presentations_date):
    presentation_date = _get_presentations_date(presentations_date)
    if request.method == "POST":
        form = PresentationForm(cinema_id, presentation_date, request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('ajax/presentation_add_success.html', {
                    'cinema_id': cinema_id,
                    'presentations_date': presentations_date
                },
                context_instance=RequestContext(request))
        else:
            raise Exception("Form contains errors: %s" % form.errors)
    else:
        form = PresentationForm(cinema_id, presentation_date)

    return render_to_response('ajax/presentation_add.html', {
            'form': form,
            'cinema_id': cinema_id,
            'presentations_date': presentations_date
        },
        context_instance=RequestContext(request))

def presentation_delete(request, cinema_id, presentations_date, presentation_id):
    context = {
        'cinema_id': cinema_id,
        'presentations_date': presentations_date,
        'presentation_id': presentation_id
    }
    if request.method == "POST":
        form = ConfirmationForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirmed']:
            presentation = get_object_or_404(Presentation, id=presentation_id, cinema__id=cinema_id)
            presentation.delete()
            return render_to_response('ajax/presentation_delete_success.html', 
                context,
                context_instance=RequestContext(request))
    return render_to_response('ajax/presentation_delete.html',
        context,
        context_instance=RequestContext(request))     