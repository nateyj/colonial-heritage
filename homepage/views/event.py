from django.http import Http404, HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.forms.extras import widgets
from django.utils import timezone
from django.contrib.auth.decorators import permission_required
from homepage.customform import CustomForm

templater = get_renderer('homepage')



#########################################################################
### Show list of people

@view_function
@permission_required('homepage.view_event', login_url='/homepage/login/')
def process_request(request):
    params = {}

    params["events"] = hmod.Event.objects.all().order_by('name')

    return templater.render_to_response(request, 'event.html', params)


#########################################################################
### Edit an event

@view_function
@permission_required('homepage.change_event', login_url='/homepage/login/')
def edit(request):
    params = {}

    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect('/homepage/event/')

    form = EventEditForm(request, initial={
        'name': event.name,
        'start_date': event.start_date,
        'end_date': event.end_date,
        'map_file_name': event.map_file_name,
    })

    if request.method == 'POST':
        form = EventEditForm(request, request.POST)  # POST is a dictionary of all the data sent with the form
        if form.is_valid():
            event.name = form.cleaned_data['name']
            event.start_date = form.cleaned_data['start_date']
            event.end_date = form.cleaned_data['end_date']
            event.map_file_name = form.cleaned_data['map_file_name']
            event.save()
            return HttpResponseRedirect('/homepage/event/')

    params['form'] = form

    return templater.render_to_response(request, 'event.edit.html', params)


class EventEditForm(CustomForm):
    this_year = timezone.now().year

    name = forms.CharField(max_length=100, required=False)
    start_date = forms.DateField(widget=forms.extras.widgets.SelectDateWidget(years=range(this_year, this_year + 10)))
    end_date = forms.DateField(widget=forms.extras.widgets.SelectDateWidget(years=range(this_year, this_year + 10)))
    map_file_name = forms.FileField(required=False)

    def clean_name(self):
        event_count = hmod.Event.objects.filter(name=self.cleaned_data['name']).exclude(
            id=self.request.urlparams[0]).count()
        if event_count >= 1:
            raise forms.ValidationError('There is already an event with this name.')

        return self.cleaned_data['name']


@view_function
@permission_required('homepage.add_event', login_url='/homepage/login/')
def create(request):
    event = hmod.Event()
    event.name = ''
    event.save()

    return HttpResponseRedirect('/homepage/event.edit/{}/new/'.format(event.id))


@view_function
@permission_required('homepage.delete_event', login_url='/homepage/login/')
def delete(request):
    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect('/homepage/event/')

    event.delete()

    return HttpResponseRedirect('/homepage/event/')