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

    params["products"] = hmod.Product.objects.all().order_by('product_specification__category', 'product_specification__name')

    return templater.render_to_response(request, 'product.html', params)


#########################################################################
### Edit a product

@view_function
# @permission_required('homepage.change_product', login_url='/homepage/login/')
def edit(request):
    params = {}
    product_id_str = request.urlparams[1]

    if request.urlparams[0] == 'new':
        # print("It is a new product")
        form = ProductEditForm()
    else:
        # print("I'm editing an existing product")
        try:
            product = hmod.Product.objects.get(id=product_id_str)
        except hmod.Product.DoesNotExist:
            return HttpResponseRedirect('/homepage/product/')

        form = ProductEditForm(initial={
            'name': product.product_specification.name,
            'description': product.product_specification.description,
            'category': product.product_specification.category,
            'price': product.product_specification.price,
            'qty_on_hand': product.qty_on_hand,
            # 'producer': product.producer,
        })

    if request.method == 'POST':
        form = ProductEditForm(request.POST)  # POST is a dictionary of all the data sent with the form

        if form.is_valid():
            name = form.cleaned_data['name']
            category_str = form.cleaned_data['category']
            desc = form.cleaned_data['description']
            price = form.cleaned_data['price']
            qty_on_hand = form.cleaned_data['qty_on_hand']
            # producer_str = form.cleaned_data['producer']

            try:
                category = hmod.Category.objects.get(name=category_str)
            except hmod.Category.DoesNotExist:
                raise forms.ValidationError("Category doesn't exist")

            if request.urlparams[0] == 'new':
                ps = hmod.ProductSpecification()
                ps.name = name
                ps.category = category
                ps.description = desc
                ps.price = price
                ps.save()

                product = hmod.Product()
                product.qty_on_hand = qty_on_hand
                product.product_specification = ps
                product.save()
            else:
                try:
                    product = hmod.Product.objects.get(id=product_id_str)
                except hmod.Product.DoesNotExist:
                    return HttpResponseRedirect('/homepage/product/')

                product.product_specification.name = name
                product.product_specification.category = category
                product.product_specification.description = desc
                product.product_specification.price = price
                product.product_specification.save()

                product.qty_on_hand = qty_on_hand
                product.save()

            # try:
            #     producer = hmod.Organization.objects.get(given_name=form.cleaned_data['producer'])
            # except hmod.Organization.DoesNotExist:
            #     raise forms.ValidationError("Producer doesn't exist")
            # product.producer = producer
            # product.save()
            return HttpResponseRedirect('/homepage/product/')

    params['form'] = form

    return templater.render_to_response(request, 'product.edit.html', params)


class ProductEditForm(forms.Form):
    name = forms.CharField(label="Name*", max_length=100)
    description = forms.CharField(max_length=100, required=False)
    category = forms.ModelChoiceField(label="Category*", queryset=hmod.Category.objects, empty_label=None)
    price = forms.DecimalField(label="Price*",max_digits=10, decimal_places=2)
    qty_on_hand = forms.IntegerField(label="Quantity On Hand*")
    # producer = forms.ModelChoiceField(queryset=hmod.Organization.objects)
    # empty_label in a ModelChoiceField will not let you continue on past the clean if that field is required

    # def clean_producer(self):
    #     try:
    #         producer = hmod.Organization.objects.get(given_name=self.cleaned_data['producer'])
    #     except hmod.Organization.DoesNotExist:
    #         raise forms.ValidationError('The producer you entered does not exist.')
    #
    #     if producer.city == 'temp':
    #         raise forms.ValidationError('You must enter a producer for this product.')
    #     return self.cleaned_data['producer']


# @view_function
# # @permission_required('homepage.add_product', login_url='/homepage/login/')
# def create(request):
#     product = hmod.Product()
#     product.name = ''
#     product.category = ''
#     product.current_price = 0
#
#     try:
#         product.producer = hmod.Organization.objects.get(city='temp')
#     except hmod.Product.DoesNotExist:
#         raise forms.ValidationError("The temporary producer doesn't exist.")
#
#     product.save()
#
#     return HttpResponseRedirect('/homepage/product.edit/{}/new/'.format(product.id))


@view_function
# @permission_required('homepage.add_product', login_url='/homepage/login/')
def delete(request):
    # delete a product before product specification

    try:
        product = hmod.Product.objects.get(id=request.urlparams[0])
    except hmod.Product.DoesNotExist:
        return HttpResponseRedirect('/homepage/product/')

    ps = product.product_specification

    product.delete()

    if hmod.Product.objects.filter(product_specification=ps).count() != 0:
        ps.delete()

    return HttpResponseRedirect('/homepage/product/')