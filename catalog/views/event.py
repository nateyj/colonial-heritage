from django.http import Http404, HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.forms.extras import widgets
from django.utils import timezone
from django.contrib.auth.decorators import permission_required
from homepage.customform import CustomForm

templater = get_renderer('catalog')



#########################################################################
### Show list of events

@view_function
def process_request(request):
    params = {}

    try:
        public_event = hmod.PublicEvent.objects.get(name='Colonial Heritage Festival')
    except hmod.PublicEvent.DoesNotExist:
        return HttpResponseRedirect('/catalog/')

    area_list = public_event.areas.all()
    # print(event_list[0])
    # print(public_event.events.all()[0])

    params["public_event"] = public_event
    params['areas'] = area_list
    params['event'] = public_event.events.all()[0]
    params['public_event_photo'] = public_event.public_event_photos.all()[0]

    return templater.render_to_response(request, 'event.html', params)


@view_function
def area_detail(request):
    params = {}

    try:
        area = hmod.Area.objects.get(name=request.urlparams[0])
    except hmod.Area.DoesNotExist:
        return HttpResponseRedirect('/catalog/event/')

    for artisan_item in area.artisan_items.all():
        print(artisan_item.artisan_item_photos.all()[0])

    params['area'] = area

    return templater.render_to_response(request, 'area_detail.html', params)