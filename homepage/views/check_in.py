from django.http import Http404, HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required
from django.forms.extras import widgets
from django.utils import timezone
from django.core.mail import send_mail

templater = get_renderer('catalog')

###################################################################
#####
@view_function
def process_request(request):
    params = {}

    return HttpResponse('Success')