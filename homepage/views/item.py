from django.http import Http404, HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from homepage.customform import CustomForm
from django.contrib.auth.decorators import permission_required

templater = get_renderer('homepage')


@view_function
@permission_required('homepage.view_item', login_url='/homepage/login/')
def process_request(request):
    params = {}
    params["items"] = hmod.Item.objects.all().order_by('name', 'value')

    return templater.render_to_response(request, 'item.html', params)


#########################################################################
### Edit an item

@view_function
@permission_required('homepage.change_item', login_url='/homepage/login/')
def edit(request):
    params = {}
    try:
        item = hmod.Item.objects.get(id=request.urlparams[0])
    except hmod.Item.DoesNotExist:
        return HttpResponseRedirect('/homepage/item/')

    form = ItemEditForm(initial={
        'Name': item.name,
        'Description': item.description,
        'Value': item.value,
        'is_rentable': item.is_rentable,
        'Rental_Price': item.standard_rental_price,
        'Owner': item.owner,
    })

    if request.method == 'POST':
        form = ItemEditForm(request.POST)  # POST is a dictionary of all the data sent with the form
        if form.is_valid():
            item.name = form.cleaned_data['Name']
            item.description = form.cleaned_data['Description']
            item.value = form.cleaned_data['Value']
            item.is_rentable = form.cleaned_data['is_rentable']
            item.standard_rental_price = form.cleaned_data['Rental_Price']
            try:
                owner = hmod.LegalEntity.objects.get(given_name=form.cleaned_data['Owner'])
            except hmod.LegalEntity.DoesNotExist:
                raise forms.ValidationError("Owner doesn't exist")
            item.owner = owner
            item.save()
            return HttpResponseRedirect('/homepage/item/')

    params['form'] = form

    return templater.render_to_response(request, 'item.edit.html', params)


class ItemEditForm(forms.Form):
    Name = forms.CharField(max_length=100)
    Description = forms.CharField(max_length=100, required=False)
    Value = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    is_rentable = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    Rental_Price = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    Owner = forms.ModelChoiceField(empty_label=None, queryset=hmod.LegalEntity.objects)

    def clean_Owner(self):
        try:
            legal_entity = hmod.LegalEntity.objects.get(given_name=self.cleaned_data['Owner'])
        except hmod.LegalEntity.DoesNotExist:
            raise forms.ValidationError('The owner you entered does not exist.')

        if legal_entity.city == 'temp':
            raise forms.ValidationError('You must enter an owner for this item.')
        return self.cleaned_data['Owner']


@view_function
@permission_required('homepage.add_item', login_url='/homepage/login/')
def create(request):
    item = hmod.Item()
    item.name = ''
    item.description = ''
    item.value = 0
    item.is_rentable = False

    try:
        item.owner = hmod.LegalEntity.objects.get(city='temp')
    except hmod.LegalEntity.DoesNotExist:
        return HttpResponseRedirect('/homepage/item/')

    item.save()

    return HttpResponseRedirect('/homepage/item.edit/{}/new/'.format(item.id))


@view_function
@permission_required('homepage.delete_item', login_url='/homepage/login/')
def delete(request):
    try:
        item = hmod.Item.objects.get(id=request.urlparams[0])
    except hmod.Item.DoesNotExist:
        return HttpResponseRedirect('/homepage/item/')

    item.delete()

    return HttpResponseRedirect('/homepage/item/')