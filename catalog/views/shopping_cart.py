from django.http import Http404, HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required

templater = get_renderer('catalog')

SHOPPING_CART_KEY = 'shopping_cart'

###################################################################
##### View shopping cart
@view_function
def process_request(request):
    params = {}

    # ensures users has a shopping cart in the session even if they haven't added any products to the cart yet
    if 'shopping_cart' not in request.session:
        request.session[SHOPPING_CART_KEY] = {}

    # 'shopping_cart' is the key in this dictionary with values waiting to be assigned
    # the value of the 'shopping_cart' key is a dictionary, which holds more keys and associated values
    params['shopping_cart'] = {}

    # a key in the shopping cart is the product ID. With the key, I can query for the product object itself
    for key in request.session[SHOPPING_CART_KEY]:

        try:
            product = hmod.Product.objects.get(id=key)
        except hmod.Product.DoesNotExist:
            return HttpResponseRedirect('/catalog/index')

        qty = request.session[SHOPPING_CART_KEY][key]

        params['shopping_cart'][product] = qty

    return templater.render_to_response(request, 'shopping_cart.html', params)


###################################################################
##### Add items to the shopping cart
@view_function
def add(request):
    product_id = request.urlparams[0]

    # URL will return the quantity as a string so we need to convert it to an int
    qty = int(request.urlparams[1])

    # ensure we have a shopping cart in the session
    if SHOPPING_CART_KEY not in request.session:
        request.session[SHOPPING_CART_KEY] = {}

    # add product to shopping cart
    if product_id in request.session[SHOPPING_CART_KEY]:
        request.session[SHOPPING_CART_KEY][product_id] += qty
    else:
        request.session[SHOPPING_CART_KEY][product_id] = qty

    request.session.modified = True

    return HttpResponseRedirect('/catalog/shopping_cart/')


###################################################################
##### Remove an item from the shopping cart
@view_function
def remove(request):
    product_id = request.urlparams[0]
    del request.session[SHOPPING_CART_KEY][product_id]

    request.session.modified = True

    return HttpResponseRedirect('/catalog/shopping_cart/')


###################################################################
##### Checkout Form
class CheckoutForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)
