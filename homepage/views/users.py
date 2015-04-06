from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from homepage.customform import CustomForm
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required, login_required


templater = get_renderer('homepage')


@view_function
@permission_required('homepage.view_siteuser', login_url='/homepage/login/')
def process_request(request):
    params = {}
    users = hmod.SiteUser.objects.all().order_by('first_name', 'last_name')

    params["users"] = users

    return templater.render_to_response(request, 'users.html', params)


@view_function
# @permission_required('homepage.change_siteuser', login_url='/homepage/login/')
def edit(request):
    params = {}
    try:
        site_user = hmod.SiteUser.objects.get(id=request.urlparams[0])
    except hmod.SiteUser.DoesNotExist:
        return HttpResponseRedirect('/homepage/users/')

    form = SiteUserEditForm(request, initial={
        'first_name': site_user.first_name,
        'last_name': site_user.last_name,
        'username': site_user.username,
        'password': site_user.password,
        'security_question': site_user.security_question,
        'security_answer': site_user.security_answer,
        'email': site_user.email,
        'authorization': site_user.groups.all()[0],
    })

    if request.method == 'POST':
        form = SiteUserEditForm(request, request.POST)  # POST is a dictionary of all the data sent with the form
        if form.is_valid():
            site_user.first_name = form.cleaned_data['first_name']
            site_user.last_name = form.cleaned_data['last_name']
            site_user.username = form.cleaned_data['username']
            site_user.set_password(form.cleaned_data['password'])
            site_user.security_question = form.cleaned_data['security_question']
            site_user.security_answer = form.cleaned_data['security_answer']
            site_user.email = form.cleaned_data['email']

            site_user.groups.clear()  # remove user from all current groups before adding them to the new group

            authorization = Group.objects.get(name=form.cleaned_data['authorization'])
            site_user.groups.add(authorization)

            site_user.save()
            return HttpResponseRedirect('/homepage/users/')

    params['form'] = form

    return templater.render_to_response(request, 'users.edit.html', params)


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
    username = forms.CharField(min_length=6, max_length=100)
    password = forms.CharField(min_length=4, max_length=100, widget=forms.PasswordInput)
    security_question = forms.ChoiceField(label='Security Question', choices=SECURITY_QUESTION_CHOICES,
                                          widget=forms.Select)
    security_answer = forms.CharField(label='Security Answer', max_length=50)
    email = forms.EmailField(max_length=50)
    authorization = forms.ModelChoiceField(label='Authorization', queryset=Group.objects.all().order_by('name'),
                                           widget=forms.RadioSelect, empty_label=None)

    def clean_username(self):
        site_users_count = hmod.SiteUser.objects.filter(username=self.cleaned_data['username']).exclude(
            id=self.request.urlparams[0]).count()
        if site_users_count >= 1:
            raise forms.ValidationError('This username is already being used.')

        return self.cleaned_data['username']


@view_function
# @permission_required('homepage.add_siteuser', login_url='/homepage/login/')
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

    try:
        authorization = Group.objects.get(name='Guest')
    except Group.DoesNotExist:
        return HttpResponseRedirect('/homepage/users/')

    site_user.groups.add(authorization)
    site_user.save()

    return HttpResponseRedirect('/homepage/users.edit/{}/new/'.format(site_user.id))


@view_function
@permission_required('homepage.delete_siteuser', login_url='/homepage/login/')
def delete(request):
    try:
        site_user = hmod.SiteUser.objects.get(id=request.urlparams[0])
    except hmod.SiteUser.DoesNotExist:
        return HttpResponseRedirect('/homepage/users/')
    site_user.delete()

    return HttpResponseRedirect('/homepage/users/')