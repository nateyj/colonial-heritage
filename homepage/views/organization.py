from django.http import Http404, HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required

templater = get_renderer('homepage')



#########################################################################
### Show list of organizations

@view_function
# @permission_required('homepage.view_legalentity', login_url='/homepage/login/')
def process_request(request):
    params = {}

    # params["organizations"] = hmod.PhotographableThing.objects.instance_of(hmod.LegalEntity).not_instance_of(hmod.Person)
    params["organizations"] = hmod.Organization.objects.all().exclude(id__in=(hmod.Person.objects.all())).order_by(
        'given_name')

    return templater.render_to_response(request, 'organization.html', params)


#########################################################################
### Edit an organization

@view_function
# @permission_required('homepage.change_legalentity', login_url='/homepage/login/')
def edit(request):
    params = {}

    try:
        organization = hmod.Organization.objects.get(id=request.urlparams[0])
    except hmod.Organization.DoesNotExist:
        return HttpResponseRedirect('/homepage/organization/')

    form = OrganizationEditForm(initial={
        'Name': organization.given_name,
        'Address': organization.address.address1,
        'City': organization.address.city,
        'State': organization.address.state,
        'ZIP': organization.address.zip_code,
        'country': organization.address.country,
        'Email': organization.email,
    })

    if request.method == 'POST':
        form = OrganizationEditForm(request.POST)  # POST is a dictionary of all the data sent with the form

        if form.is_valid():
            organization.given_name = form.cleaned_data['Name']
            organization.address.address1 = form.cleaned_data['Address']
            organization.address.city = form.cleaned_data['City']
            organization.address.state = form.cleaned_data['State']
            organization.address.zip_code = form.cleaned_data['ZIP']
            organization.address.country = form.cleaned_data['country']
            organization.email = form.cleaned_data['Email']
            organization.address.save()
            organization.save()

            return HttpResponseRedirect('/homepage/organization/')

    params['form'] = form

    return templater.render_to_response(request, 'organization.edit.html', params)


class OrganizationEditForm(forms.Form):
    ALASKA = 'AK'
    ALABAMA = 'AL'
    ARKANSAS = 'AR'
    ARIZONA = 'AZ'
    CALIFORNIA = 'CA'
    COLORADO = 'CO'
    CONNECTICUT = 'CT'
    DELAWARE = 'DE'
    FLORIDA = 'FL'
    GEORGIA = 'GA'
    HAWAII = 'HI'
    IOWA = 'IA'
    IDAHO = 'ID'
    ILLINOIS = 'IL'
    INDIANA = 'IN'
    KANSAS = 'KS'
    LOUISIANA = 'LA'
    MASSACHUSETTS = 'MA'
    MARYLAND = 'MD'
    MAINE = 'ME'
    MICHIGAN = 'MI'
    MINNESOTA = 'MN'
    MISSOURI = 'MO'
    MISSISSIPPI = 'MS'
    MONTANA = 'MT'
    NORTH_CAROLINA = 'NC'
    NORTH_DAKOTA = 'ND'
    NEBRASKA = 'NE'
    NEW_HAMPSHIRE = 'NH'
    NEW_JERSEY = 'NJ'
    NEW_MEXICO = 'NM'
    NEVADA = 'NV'
    NEW_YORK = 'NY'
    OHIO = 'OH'
    OKLAHOMA = 'OK'
    OREGON = 'OR'
    PENNSYLVANIA = 'PA'
    RHODE_ISLAND = 'RI'
    SOUTH_CAROLINA = 'SC'
    SOUTH_DAKOTA = 'SD'
    TENNESSEE = 'TN'
    TEXAS = 'TX'
    UTAH = 'UT'
    VIRGINIA = 'VA'
    VERMONT = 'VT'
    WASHINGTON = 'WA'
    WISCONSIN = 'WI'
    WEST_VIRGINIA = 'WV'
    WYOMING = 'WY'

    # Choices list of tuples for the car_states field
    STATE_CHOICES = (
        (ALASKA, 'AK'),
        (ALABAMA, 'AL'),
        (ARKANSAS, 'AR'),
        (ARIZONA, 'AZ'),
        (CALIFORNIA, 'CA'),
        (COLORADO, 'CO'),
        (CONNECTICUT, 'CT'),
        (DELAWARE, 'DE'),
        (FLORIDA, 'FL'),
        (GEORGIA, 'GA'),
        (HAWAII, 'HI'),
        (IOWA, 'IA'),
        (IDAHO, 'ID'),
        (ILLINOIS, 'IL'),
        (INDIANA, 'IN'),
        (KANSAS, 'KS'),
        (LOUISIANA, 'LA'),
        (MASSACHUSETTS, 'MA'),
        (MARYLAND, 'MD'),
        (MAINE, 'ME'),
        (MICHIGAN, 'MI'),
        (MINNESOTA, 'MN'),
        (MISSOURI, 'MO'),
        (MISSISSIPPI, 'MI'),
        (MONTANA, 'MT'),
        (NORTH_CAROLINA, 'NC'),
        (NORTH_DAKOTA, 'ND'),
        (NEBRASKA, 'NE'),
        (NEW_HAMPSHIRE, 'NH'),
        (NEW_JERSEY, 'NJ'),
        (NEW_MEXICO, 'NM'),
        (NEVADA, 'NV'),
        (NEW_YORK, 'NY'),
        (OHIO, 'OH'),
        (OKLAHOMA, 'OK'),
        (OREGON, 'OR'),
        (PENNSYLVANIA, 'PA'),
        (RHODE_ISLAND, 'RI'),
        (SOUTH_CAROLINA, 'SC'),
        (SOUTH_DAKOTA, 'SD'),
        (TENNESSEE, 'TN'),
        (TEXAS, 'TX'),
        (UTAH, 'UT'),
        (VIRGINIA, 'VA'),
        (VERMONT, 'VT'),
        (WASHINGTON, 'WA'),
        (WISCONSIN, 'WI'),
        (WEST_VIRGINIA, 'WV'),
        (WYOMING, 'WY'),
    )

    Name = forms.CharField(min_length=3, max_length=100)
    Address = forms.CharField(max_length=100)
    City = forms.CharField(max_length=50)
    State = forms.ChoiceField(widget=forms.Select, choices=STATE_CHOICES)
    ZIP = forms.CharField(max_length=5)
    country = forms.CharField(max_length=50, required=False)
    Email = forms.EmailField(required=False, max_length=100)

    def clean_ZIP(self):
        if len(self.cleaned_data['ZIP']) != 5:
            raise forms.ValidationError('Please enter a valid ZIP code.')
        return self.cleaned_data['ZIP']


#########################################################################
### Create an organization

@view_function
# @permission_required('homepage.add_legalentity', login_url='/homepage/login/')
def create(request):
    address = hmod.Address()
    address.address1 = ''
    address.city = ''
    address.state = ''
    address.zip_code = ''
    address.save()

    organization = hmod.Organization()
    organization.given_name = ''
    organization.email = ''
    organization.address = address
    organization.save()

    return HttpResponseRedirect('/homepage/organization.edit/{}/new/'.format(organization.id))


#########################################################################
### Delete an organization

@view_function
# @permission_required('homepage.delete_legalentity', login_url='/homepage/login/')
def delete(request):
    org_id = request.urlparams[0]
    try:
        organization = hmod.Organization.objects.get(id=org_id)
    except hmod.Organization.DoesNotExist:
        return HttpResponseRedirect('/homepage/organization/')

    address = organization.address

    # list of organizations with the same address as the person being deleted excluding this person
    org_list = hmod.Organization.objects.filter(address=address).exclude(id=org_id)
    ven_list = hmod.Venue.objects.filter(address=address)
    trans_list = hmod.Transaction.objects.filter(ships_to=address)

    organization.delete()

    if org_list.count() == 0 and trans_list.count() == 0 and ven_list.count() == 0:
        address.delete()

    return HttpResponseRedirect('/homepage/organization/')