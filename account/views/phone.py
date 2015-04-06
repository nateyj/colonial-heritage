from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from homepage.customform import CustomForm
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import authenticate, login, logout


templater = get_renderer('account')


@view_function
def edit(request):
    params = {}

    try:
        phone = hmod.Phone.objects.get(id=request.urlparams[0])
    except hmod.Phone.DoesNotExist:
        return HttpResponseRedirect('/account/account/')

    form = PhoneEditForm(initial={
        'number': phone.number,
        'ext': phone.extension,
        'type': phone.type,
    })

    if request.method == 'POST':
        form = PhoneEditForm(request.POST)

        if form.is_valid():
            phone.number = form.cleaned_data['number']
            phone.extension = form.cleaned_data['ext']
            phone.type = form.cleaned_data['type']
            phone.save()

            return HttpResponseRedirect('/account/account/')

    params['form'] = form

    return templater.render_to_response(request, 'phone.edit.html', params)


class PhoneEditForm(forms.Form):
    MOBILE = 'mobile'
    HOME = 'home'
    WORK = 'work'
    OFFICE = 'office'

    PHONE_TYPE_CHOICES = (
        (MOBILE, 'Mobile'),
        (HOME, 'Home'),
        (WORK, 'Work'),
        (OFFICE, 'Office'),
    )

    number = forms.CharField(label="Phone")
    ext = forms.IntegerField(required=False)
    type = forms.ChoiceField(widget=forms.Select, choices=PHONE_TYPE_CHOICES, initial=MOBILE)


class PhoneChangeForm(forms.Form):
    phone = forms.ModelChoiceField(queryset=hmod.Phone.objects.all(), widget=forms.RadioSelect)


@view_function
def create(request):
    phone = hmod.Phone()
    phone.number = ''
    phone.type = 'mobile'
    phone.user = request.user
    phone.save()

    return HttpResponseRedirect('/account/account.edit/{}/new/'.format(phone.id))


@view_function
def delete(request):
    try:
        phone = hmod.Phone.objects.get(id=request.urlparams[0])
    except hmod.Phone.DoesNotExist:
        return HttpResponseRedirect('/account/account/')

    phone.delete()

    return HttpResponseRedirect('/account/account/')

# @view_function
# def change(request):
# params = {}
#
#     try:
#         user = hmod.SiteUser.objects.get(id=request.urlparams[0])
#     except hmod.SiteUser.DoesNotExist:
#         return HttpResponseRedirect('/account/account/')
#
#     form = PhoneChangeForm()
#
#     if request.method == 'POST':
#         form = PhoneChangeForm(request.POST)
#
#         if form.is_valid():
#             return HttpResponseRedirect('/catalog/shipping/{}/{}/{}/'.format(user.id, address.id, phone.id))
#
#     return templater.render_to_response(request, 'phone.change.html', params)

