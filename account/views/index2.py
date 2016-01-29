__author__ = 'Nate'

from django.contrib.auth import authenticate, login, logout
from django import forms
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
# from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO
import homepage.models as hmod


templater = get_renderer('account')


@view_function
def process_request(request):
    params = {}

    return templater.render_to_response(request, 'index2.html', params)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)

    def clean(self):
        if self.is_valid():
            if len(self.cleaned_data['username']) < 6:
                raise forms.ValidationError("Your username must be at least 6 characters.")

            if len(self.cleaned_data['password']) < 4:
                raise forms.ValidationError("Your password must be at least 4 characters.")

                # user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
                #
                # if user == None:
                # raise forms.ValidationError("The username or password you entered was incorrect.")

        return self.cleaned_data


#########################################################################
### Logs a user out

@view_function
def logout_view(request):
    logout(request)

    return HttpResponseRedirect('/catalog/index')


#########################################################################
### Displays login Form in the modal

@view_function
def loginform(request):
    params = {}
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)  # redisplays page with posted information

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # active directory is the master and our account on our system is mimicking that

            # is this a valid user?
            # for Server put 'yourserver.com'
            s = Server('byuldap.byu.edu', port=389, get_info=GET_ALL_INFO)
            # put the user's password in the password parameter
            c = Connection(s, auto_bind=True, client_strategy=STRATEGY_SYNC, user='cn=%s,ou=people,o=ces' % username,
                           password=password, authentication=AUTH_SIMPLE)

            if c != None:
                print(c)

                # # now that we know it is a valid user, get the user account from Django
                # u = hmod.SiteUser.objects.get_or_create(username=username)
                # u.first_name = # the info is in the c object c.something
                # u.last_name =
                # u.email =
                # u.set_password(password)
                # u.save()

                user = authenticate(username=username, password=password)
                login(request, user)
            else:
                user = authenticate(username=username, password=password)
                login(request, user)

            return HttpResponse('''
                <script>
                    window.location.href = window.location.href;
                </script>
            ''')

    params['form'] = form

    return templater.render_to_response(request, 'whatever.html', params)


#########################################################################
### Sends an email to the user to enable them to reset their password

@view_function
def send_email(request):
    pass