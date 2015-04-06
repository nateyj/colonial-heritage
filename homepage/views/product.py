from django.http import Http404, HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required

templater = get_renderer('homepage')


@view_function
@permission_required('homepage.view_product', login_url='/homepage/login/')
def process_request(request):
    params = {}

    params["products"] = hmod.Product.objects.all().order_by('name', 'category')

    return templater.render_to_response(request, 'product.html', params)


#########################################################################
### Edit a product

@view_function
@permission_required('homepage.change_product', login_url='/homepage/login/')
def edit(request):
    params = {}

    try:
        product = hmod.Product.objects.get(id=request.urlparams[0])
    except hmod.Product.DoesNotExist:
        return HttpResponseRedirect('/homepage/product/')

    form = ProductEditForm(initial={
        'name': product.name,
        'description': product.description,
        'category': product.category,
        'current_price': product.current_price,
        'producer': product.producer,
    })

    if request.method == 'POST':
        form = ProductEditForm(request.POST)  # POST is a dictionary of all the data sent with the form
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.current_price = form.cleaned_data['current_price']
            try:
                producer = hmod.LegalEntity.objects.get(given_name=form.cleaned_data['producer'])
            except hmod.LegalEntity.DoesNotExist:
                raise forms.ValidationError("Producer doesn't exist")
            product.producer = producer
            product.save()
            return HttpResponseRedirect('/homepage/product/')

    params['form'] = form

    return templater.render_to_response(request, 'product.edit.html', params)


class ProductEditForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100, required=False)
    category = forms.CharField(max_length=100)
    current_price = forms.DecimalField(label='Current Price', max_digits=10, decimal_places=2)
    producer = forms.ModelChoiceField(empty_label=None, queryset=hmod.LegalEntity.objects)

    def clean_producer(self):
        try:
            producer = hmod.LegalEntity.objects.get(given_name=self.cleaned_data['producer'])
        except hmod.LegalEntity.DoesNotExist:
            raise forms.ValidationError('The producer you entered does not exist.')

        if producer.city == 'temp':
            raise forms.ValidationError('You must enter a producer for this product.')
        return self.cleaned_data['producer']


@view_function
@permission_required('homepage.add_product', login_url='/homepage/login/')
def create(request):
    product = hmod.Product()
    product.name = ''
    product.category = ''
    product.current_price = 0

    try:
        product.producer = hmod.LegalEntity.objects.get(city='temp')
    except hmod.Product.DoesNotExist:
        raise forms.ValidationError("The temporary producer doesn't exist.")

    product.save()

    return HttpResponseRedirect('/homepage/product.edit/{}/new/'.format(product.id))


@view_function
@permission_required('homepage.add_product', login_url='/homepage/login/')
def delete(request):
    try:
        product = hmod.Product.objects.get(id=request.urlparams[0])
    except hmod.Product.DoesNotExist:
        return HttpResponseRedirect('/homepage/product/')

    product.delete()

    return HttpResponseRedirect('/homepage/product/')