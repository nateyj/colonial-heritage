from django.http import Http404, HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required
from django.utils import timezone
from django.contrib.auth import authenticate

templater = get_renderer('homepage')


#########################################################################
### View all of a user's rental items that have not yet been checked in
@view_function
def process_request(request):
    params = {}

    # determine who the user is
    # username = request.urlparams[0]

    try:
        # site_user = hmod.SiteUser.objects.get(username=username)
        site_user = hmod.SiteUser.objects.get(id=4)
    except hmod.SiteUser.DoesNotExist:
        return HttpResponseRedirect('/homepage/index/')

    params["rental_items"] = site_user.get_checked_out_rental_items()

    return templater.render_to_response(request, 'rental_items.html', params)


class UsernameForm(forms.Form):
    username = forms.CharField()

    def clean_username(self):
        try:
            site_user = hmod.SiteUser.objects.get(username=self.cleaned_data['username'])
        except hmod.SiteUser.DoesNotExist:
            raise forms.ValidationError("There is no user with that username. Please try again.")

        user = authenticate(username=self.cleaned_data['username'], password=site_user.password)

        if user == None:
            raise forms.ValidationError("There is no user with that username. Please try again.")

        return self.cleaned_data['username']


@view_function
def verify_account(request):
    params = {}

    form = UsernameForm()

    if request.method == 'POST':
        form = UsernameForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']

            try:
                site_user = hmod.SiteUser.objects.get(username=username)
            except hmod.SiteUser.DoesNotExist:
                raise forms.ValidationError("There is no user with that username. Please try again.")

            user = authenticate(username=username, password=site_user.password)

            if user != None:
                params['username'] = user

            return HttpResponseRedirect('/homepage/rental_items/')

    site_user = params['username']

    return HttpResponseRedirect('/homepage/rental_items/{}'.format(site_user.id))


###################################################################
#####
@view_function
def check_in(request):
    params = {}

    return HttpResponse('Success')