from django.http import Http404, HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.forms.extras import widgets
from django.contrib.auth.decorators import permission_required
from django.utils import timezone

templater = get_renderer('homepage')



#########################################################################
### Show list of people

@view_function
# @permission_required('homepage.view_person', login_url='/homepage/login/')
def process_request(request):
    params = {}

    params["people"] = hmod.Person.objects.all().order_by('last_name', 'given_name')

    return templater.render_to_response(request, 'person.html', params)


#########################################################################
### Edit a person

@view_function
# @permission_required('homepage.change_person', login_url='/homepage/login/')
def edit(request):
    params = {}

    try:
        person = hmod.Person.objects.get(id=request.urlparams[0])
    except hmod.Person.DoesNotExist:
        return HttpResponseRedirect('/homepage/person/')

    # if the person has no phone numbers tied to them
    if person.org_phones.count() != 0:
        phone = person.org_phones.all()[0]  #just get the first phone number tied to this person

        form = PersonEditForm(initial={
            'First_Name': person.given_name,
            'Last_Name': person.last_name,
            'Birth_Date': person.birth_date,
            'Address': person.address.address1,
            'City': person.address.city,
            'State': person.address.state,
            'ZIP': person.address.zip_code,
            'country': person.address.country,
            'number': phone.number,
            'extension': phone.extension,
            'type': phone.type,
            'Email': person.email,
        })
    else:
        form = PersonEditForm(initial={
            'First_Name': person.given_name,
            'Last_Name': person.last_name,
            'Birth_Date': person.birth_date,
            'Address': person.address.address1,
            'City': person.address.city,
            'State': person.address.state,
            'ZIP': person.address.zip_code,
            'country': person.address.country,
            'Email': person.email,
        })

    if request.method == 'POST':
        form = PersonEditForm(request.POST)  # POST is a dictionary of all the data sent with the form

        if form.is_valid():
            person.given_name = form.cleaned_data['First_Name']
            person.last_name = form.cleaned_data['Last_Name']
            person.birth_date = form.cleaned_data['Birth_Date']
            person.email = form.cleaned_data['Email']
            person.save()

            person.address.address1 = form.cleaned_data['Address']
            person.address.city = form.cleaned_data['City']
            person.address.state = form.cleaned_data['State']
            person.address.zip_code = form.cleaned_data['ZIP']
            person.address.country = form.cleaned_data['country']
            person.address.save()

            if person.org_phones.count() == 0:
                phone = hmod.Phone()
                phone.number = form.cleaned_data['number']
                phone.extension = form.cleaned_data['extension']
                phone.type = form.cleaned_data['type']
                phone.organization = person
                phone.save()
            else:
                phone = person.org_phones.all()[0]
                phone.number = form.cleaned_data['number']
                phone.extension = form.cleaned_data['extension']
                phone.type = form.cleaned_data['type']
                phone.organization = person
                phone.save()

            return HttpResponseRedirect('/homepage/person/')

    params['form'] = form

    return templater.render_to_response(request, 'person.edit.html', params)


class PersonEditForm(forms.Form):
    this_year = timezone.now().year

    MOBILE = 'mobile'
    HOME = 'home'
    WORK = 'work'
    OFFICE = 'office'

    TYPE_CHOICES = (
        (MOBILE, 'Mobile'),
        (HOME, 'Home'),
        (WORK, 'Work'),
        (OFFICE, 'Office'),
    )

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

    First_Name = forms.CharField(label='First Name*', max_length=100)
    Last_Name = forms.CharField(label='Last Name*', max_length=100)
    Birth_Date = forms.DateField(label='Birth Date', required=False, widget=forms.extras.widgets.SelectDateWidget(
        years=range(this_year - 50, this_year - 18)))
    Address = forms.CharField(label='Address*', max_length=100)
    City = forms.CharField(label='City*', max_length=50)
    State = forms.ChoiceField(label='State*', widget=forms.Select, choices=STATE_CHOICES)
    ZIP = forms.IntegerField(label='ZIP*', )
    country = forms.CharField(max_length=50, required=False)
    number = forms.CharField(label='Phone Number', required=False, max_length=15, help_text='e.g., xxx-xxx-xxxx')
    extension = forms.IntegerField(required=False)
    type = forms.ChoiceField(widget=forms.Select, choices=TYPE_CHOICES, required=False)
    Email = forms.EmailField(required=False, max_length=100)

    def clean_Last_Name(self):
        if len(self.cleaned_data['Last_Name']) < 2:
            raise forms.ValidationError('Please enter a last name at least 2 characters long.')
        return self.cleaned_data['Last_Name']

    def clean_number(self):
        if len(self.cleaned_data['number']) < 7:
            raise forms.ValidationError('Please enter a valid phone number.')
        if len(self.cleaned_data['number']) >= 7 and len(self.cleaned_data['number']) < 11:
            raise forms.ValidationError('Please include the area code.')
        return self.cleaned_data['number']


@view_function
# @permission_required('homepage.add_person', login_url='/homepage/login/')
def create(request):
    address = hmod.Address()
    address.address1 = ''
    address.city = ''
    address.state = ''
    address.zip_code = ''
    address.save()

    person = hmod.Person()
    person.given_name = ''
    person.family_name = ''
    person.email = ''
    person.address = address
    person.save()

    phone = hmod.Phone()
    phone.number = ''
    phone.type = 'mobile'
    phone.organization = person
    phone.save()

    return HttpResponseRedirect('/homepage/person.edit/{}/new/{}/'.format(person.id, phone.id))


@view_function
# @permission_required('homepage.delete_person', login_url='/homepage/login/')
def delete(request):
    # delete phone first, then organization, then address

    phone_id = request.urlparams[1]
    person_id = request.urlparams[0]

    try:
        person = hmod.Person.objects.get(id=person_id)
    except hmod.Person.DoesNotExist:
        return HttpResponseRedirect('/homepage/person/')

    # print("Found a person")
    address = person.address
    print(address)

    # list of organizations with the same address as the person being deleted excluding this person
    org_list = hmod.Organization.objects.filter(address=address).exclude(id=person_id)
    ven_list = hmod.Venue.objects.filter(address=address)
    trans_list = hmod.Transaction.objects.filter(ships_to=address)

    # print(org_list)
    # print(ven_list)
    # print(trans_list)

    if phone_id != '':
        try:
            phone = hmod.Phone.objects.get(id=phone_id)
        except hmod.Phone.DoesNotExist:
            return HttpResponseRedirect('/homepage/person/')

        phone.delete()
    else:
        for phone in person.org_phones.all():
            phone.delete()

    # print("deleted the phone numbers of this person")
    person.delete()
    # print("deleted this person!")

    # organization, venue, transaction
    if org_list.count() == 0 and trans_list.count() == 0 and ven_list.count() == 0:
        address.delete()
        print("Deleted the address associated with this person")
    else:
        print("address still tied to another organization, venue, or transaction")

    return HttpResponseRedirect('/homepage/person/')