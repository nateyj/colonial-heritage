__author__ = 'Nate'

from django.contrib.auth import authenticate, login
from django import forms
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod
from homepage.customform import CustomForm

templater = get_renderer('account')


@view_function
def process_request(request):
    params = {}

    return templater.render_to_response(request, 'index2.html', params)


class PasswordEditForm(CustomForm):
    current_password = forms.CharField(label='Current Password', widget=forms.PasswordInput, max_length=100)
    new_password = forms.CharField(label='Enter New Password', widget=forms.PasswordInput, max_length=100,
                                   help_text='Password must be at least 4 characters.')
    retype_password = forms.CharField(label='Re-type New Password', widget=forms.PasswordInput, max_length=100)

    def clean(self):
        current_password = self.cleaned_data['current_password']
        new_password = self.cleaned_data['new_password']
        site_user_id = self.request.urlparams[0]

        try:
            user = hmod.SiteUser.objects.get(id=site_user_id)
        except hmod.SiteUser.DoesNotExist:
            raise forms.ValidationError("If you see this, you're in deep kimchi.")

        if self.is_valid():
            if len(current_password) < 4:
                raise forms.ValidationError("Your current password must be at least 4 characters.")

            if not user.check_password(current_password):
                raise forms.ValidationError("The current password was entered incorrectly.")

            if len(new_password) < 4:
                raise forms.ValidationError("Your new password must be at least 4 characters.")

            if new_password != self.cleaned_data['retype_password']:
                raise forms.ValidationError("The new password you re-entered doesn't match.")

            # The current password has to be used instead of the new password the user just entered, because the user's
            # password hasn't been set to the new password yet. The setting of the new password occurs after the
            # cleaning of the form
            user = authenticate(username=user.username, password=current_password)

            if user == None:
                raise forms.ValidationError(
                    "You could not be logged in. The username or password you entered was incorrect.")

        return self.cleaned_data


class PasswordResetForm(CustomForm):
    new_password = forms.CharField(label='Enter New Password', widget=forms.PasswordInput, max_length=100,
                                   help_text='Password must be at least 4 characters.')
    retype_password = forms.CharField(label='Re-type New Password', widget=forms.PasswordInput, max_length=100)

    def clean(self):
        new_password = self.cleaned_data['new_password']
        site_user_id = self.request.urlparams[0]

        try:
            user = hmod.SiteUser.objects.get(id=site_user_id)
        except hmod.SiteUser.DoesNotExist:
            raise forms.ValidationError("If you see this, you're in deep kimchi.")

        if self.is_valid():
            if len(new_password) < 4:
                raise forms.ValidationError("Your new password must be at least 4 characters.")

            if new_password != self.cleaned_data['retype_password']:
                raise forms.ValidationError("The new password you re-entered doesn't match.")

            # The current password has to be used instead of the new password the user just entered, because the user's
            # password hasn't been set to the new password yet. The setting of the new password occurs after the
            # cleaning of the form
            user = authenticate(username=user.username, password=user.password)

            if user == None:
                raise forms.ValidationError("You could not be logged in. The password you entered was incorrect.")

        return self.cleaned_data


@view_function
def edit(request):
    params = {}
    site_user_id = request.urlparams[0]
    second_url_param = request.urlparams[1]

    try:
        site_user = hmod.SiteUser.objects.get(id=site_user_id)
    except hmod.SiteUser.DoesNotExist:
        return HttpResponseRedirect('/account/account/')

    if second_url_param == 'reset':
        form = PasswordResetForm(request)
    else:
        form = PasswordEditForm(request)

    if request.method == 'POST':
        if second_url_param == 'reset':
            form = PasswordResetForm(request, request.POST)
        else:
            form = PasswordEditForm(request, request.POST)  # POST is a dictionary of all the data sent with the form

        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            site_user.set_password(new_password)
            site_user.save()

            # after user changes or resets their password, they need to be authenticated again or they will be logged out
            user = authenticate(username=site_user.username, password=new_password)
            login(request, user)

            return HttpResponseRedirect('/account/account/')

    params['form'] = form

    return templater.render_to_response(request, 'password.edit.html', params)


@view_function
def reset_password(request):
    # yourserver.com/account/password.reset_password/site_userID/hashed-encryptedpassword
    pass