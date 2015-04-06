__author__ = 'Nate'

from django.contrib.auth import authenticate, login, logout
from django import forms
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO
import homepage.models as hmod

templater = get_renderer('homepage')


@view_function
def process_request(request):
    params = {}

    return templater.render_to_response(request, 'login.html', params)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']

            if len(username) < 4:
                raise forms.ValidationError("Your username must be at least 4 characters.")

            if len(password) < 4:
                raise forms.ValidationError("Your password must be at least 4 characters.")

            s = Server('www.westonrhodes.com', port=8889, get_info=GET_ALL_INFO)

            try:
                c = Connection(s, auto_bind=True, client_strategy=STRATEGY_SYNC,
                               user='%s@westonrhodes.local' % username, password=password, authentication=AUTH_SIMPLE)
            except:
                raise forms.ValidationError("You are not in our Active Directory.")

            if c is not None:
                # now that we know it is a valid user, get the user account from Django
                # u = hmod.SiteUser.objects.get_or_create(username=username)
                # # the info is in the c object c.something
                # u.username = c.user
                # u.first_name = c.
                # u.last_name = c.
                # u.email = c.
                # u.set_password(c.password)
                # u.save()
                print("there is a C!")
                user = authenticate(username=username, password=password)
            else:
                print("no C is floosy")
                user = authenticate(username=username, password=password)

            if user == None:
                raise forms.ValidationError("The username or password you entered was incorrect.")

        return self.cleaned_data


#########################################################################
### Logs a user out

@view_function
def logout_view(request):
    logout(request)

    return HttpResponseRedirect('/homepage/')


#########################################################################
### Checks to see if a username is available

@view_function
def check_username(request):
    # get the username from the request
    # request.REQUEST is a dictionary
    username = request.REQUEST.get('u')

    # check to see if username is already in database using hmod.SiteUser.objects.get()
    # make sure you take care of the case where I set my own username to the same username

    # if exists:
    return HttpResponse('No')

    # if not exist:
    #return HttpResponse('Yes')


#########################################################################
###

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


            # c = Connection(s, auto_bind=True, client_strategy=STRATEGY_SYNC, user='cn=%s,ou=people,o=ces' % username, password='Password1', authentication=AUTH_SIMPLE)
            # put the user's password in the password parameter



            # attribute_list = c.search(search_base='o=test', search_filter='(object_class=inetOrgPerson)', attributes='ALL_ATTRIBUTES')
            #
            # for attr in attribute_list:
            # print(attr)

            # # now that we know it is a valid user, get the user account from Django
            # u = hmod.SiteUser.objects.get_or_create(username=username)
            # # the info is in the c object c.something
            # u.username = c.user
            # u.first_name = c.
            # u.last_name = c.
            # u.email = c.
            # u.set_password(c.password)
            # u.save()

            user = authenticate(username=username, password=password)
            login(request, user)

            return HttpResponse('''
                <script>
                    window.location.href = window.location.href;
                </script>
            ''')

    params['form'] = form

    return templater.render_to_response(request, 'login.loginform.html', params)