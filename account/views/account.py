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

#########################################################################
### User views their account

@view_function
def process_request(request):
    params = {}

    # displays account info of the currently logged in user
    try:
        user = hmod.SiteUser.objects.get(id=request.user.id)
    except hmod.SiteUser.DoesNotExist:
        return HttpResponseRedirect('/catalog/index/')

    params["user"] = user

    return templater.render_to_response(request, 'account.html', params)


@view_function
def edit(request):
    params = {}
    first_urlparam = request.urlparams[0]

    if first_urlparam == 'new':
        form = SiteUserCreateForm(request)
    else:
        try:
            site_user = hmod.SiteUser.objects.get(id=request.urlparams[1])
        except hmod.SiteUser.DoesNotExist:
            return HttpResponseRedirect('/account/account/')

        form = SiteUserEditForm(request, initial={
            'first_name': site_user.first_name,
            'last_name': site_user.last_name,
            'username': site_user.username,
            'security_question': site_user.security_question,
            'security_answer': site_user.security_answer,
            'email': site_user.email,
        })

    if request.method == 'POST':
        # if they're creating their new account, we want the form with the password fields
        if first_urlparam == 'new':
            form = SiteUserCreateForm(request, request.POST)  # POST is a dictionary of all the data sent with the form
        else:
            form = SiteUserEditForm(request, request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            security_question = form.cleaned_data['security_question']
            security_answer = form.cleaned_data['security_answer']
            email = form.cleaned_data['email']

            if first_urlparam == 'new':
                site_user = hmod.SiteUser()
                site_user.first_name = first_name
                site_user.last_name = last_name
                site_user.username = username
                site_user.set_password(form.cleaned_data['password'])
                site_user.security_question = security_question
                site_user.security_answer = security_answer
                site_user.email = email
                site_user.save()

                # add the new user to the Guest group
                try:
                    authorization = Group.objects.get(name='Guest')
                except Group.DoesNotExist:
                    return HttpResponseRedirect('/account/index2/')

                site_user.groups.add(authorization)
                site_user.save()

                # after user creates an account, this will log them in upon creation
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                login(request, user)
            else:
                try:
                    site_user = hmod.SiteUser.objects.get(id=request.urlparams[1])
                except hmod.SiteUser.DoesNotExist:
                    return HttpResponseRedirect('/account/account/')

                site_user.first_name = first_name
                site_user.last_name = last_name
                site_user.username = username
                site_user.security_question = security_question
                site_user.security_answer = security_answer
                site_user.email = email
                site_user.save()

            return HttpResponseRedirect('/account/account/')

    params['form'] = form

    return templater.render_to_response(request, 'account.edit.html', params)


class SiteUserCreateForm(CustomForm):
    BIRTHDAY = "What is your oldest sibling's birthday month and year?"
    CITY = 'In what city or town did your mother and father meet?'
    KISS = 'What is the first name of the first person you kissed?'
    NICKNAME = 'What was your childhood nickname?'

    SECURITY_QUESTION_CHOICES = (
        (BIRTHDAY, "What is your oldest sibling's birthday month and year?"),
        (CITY, 'In what city or town did your mother and father meet?'),
        (KISS, 'What is the first name of the first person you kissed?'),
        (NICKNAME, 'What was your childhood nickname?'),
    )
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    username = forms.CharField(min_length=6, max_length=100, help_text='Must be 6-100 characters')
    password = forms.CharField(min_length=4, max_length=100, widget=forms.PasswordInput,
                               help_text="Must be 4-100 characters")
    retype_password = forms.CharField(label='Re-type Password', max_length=100, widget=forms.PasswordInput)
    security_question = forms.ChoiceField(label='Security Question', choices=SECURITY_QUESTION_CHOICES,
                                          widget=forms.Select)
    security_answer = forms.CharField(label='Security Answer', max_length=50)
    email = forms.EmailField(max_length=50)

    def clean(self):
        if self.is_valid():
            # checks to see if there are any other users with the username they typed in, excluding themselves if they want
            # to keep their same username
            site_users_count = hmod.SiteUser.objects.filter(username=self.cleaned_data['username']).count()

            if site_users_count >= 1:
                raise forms.ValidationError('Did you not read the red text? This username is already being used...')

            # checks to see if the passwords they entered equal each other
            if self.cleaned_data['password'] != self.cleaned_data['retype_password']:
                raise forms.ValidationError('The passwords you entered do not match.')

        return self.cleaned_data


# same as SiteUserCreateForm without the password fields
class SiteUserEditForm(CustomForm):
    BIRTHDAY = "What is your oldest sibling's birthday month and year?"
    CITY = 'In what city or town did your mother and father meet?'
    KISS = 'What is the first name of the first person you kissed?'
    NICKNAME = 'What was your childhood nickname?'

    SECURITY_QUESTION_CHOICES = (
        (BIRTHDAY, "What is your oldest sibling's birthday month and year?"),
        (CITY, 'In what city or town did your mother and father meet?'),
        (KISS, 'What is the first name of the first person you kissed?'),
        (NICKNAME, 'What was your childhood nickname?'),
    )
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    username = forms.CharField(min_length=6, max_length=100, help_text='Must be 6-100 characters')
    security_question = forms.ChoiceField(label='Security Question', choices=SECURITY_QUESTION_CHOICES,
                                          widget=forms.Select)
    security_answer = forms.CharField(label='Security Answer', max_length=50)
    email = forms.EmailField(max_length=50)

    def clean_username(self):
        site_user_id = self.request.urlparams[1]

        # checks to see if there are any other users with the username they typed in, excluding themselves if they want
        # to keep their same username
        site_users_count = hmod.SiteUser.objects.filter(username=self.cleaned_data['username']).exclude(
            id=site_user_id).count()
        if site_users_count >= 1:
            raise forms.ValidationError('Did you not read the red text? This username is already being used...')

        return self.cleaned_data['username']


@view_function
def create(request):
    site_user = hmod.SiteUser()
    site_user.first_name = ''
    site_user.last_name = ''
    site_user.username = ''
    site_user.password = ''
    site_user.security_question = ''
    site_user.security_answer = ''
    site_user.email = ''
    site_user.save()

    # add the new user to the Guest group
    try:
        authorization = Group.objects.get(name='Guest')
    except Group.DoesNotExist:
        return HttpResponseRedirect('/account/index2/')

    site_user.groups.add(authorization)
    site_user.save()

    return HttpResponseRedirect('/account/account.edit/{}/new/'.format(site_user.id))


#########################################################################
### Checks to see if a username is available

@view_function
def check_username(request):
    site_user_id = request.urlparams[0]

    # get the username from the request
    # request.REQUEST is a dictionary
    username = request.REQUEST.get('u')

    # check to see if username is already in database
    # Takes care of the case where I set my own username to the same username
    if site_user_id != '':
        site_users_count = hmod.SiteUser.objects.filter(username=username).exclude(id=site_user_id).count()
    else:
        site_users_count = hmod.SiteUser.objects.filter(username=username).count()

    if site_users_count >= 1:
        return HttpResponse('No')  # returns 'No' if username isn't available
    else:
        return HttpResponse('Yes')  # returns 'Yes' if username is available


@view_function
def delete(request):
    try:
        site_user = hmod.SiteUser.objects.get(id=request.urlparams[0])
    except hmod.SiteUser.DoesNotExist:
        return HttpResponseRedirect('/account/index2/')

    site_user.delete()

    return HttpResponseRedirect('/catalog/index/')

