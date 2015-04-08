from django.http import Http404, HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required
import time
import tkinter.messagebox as mbox
from decimal import Decimal
from django.forms.extras import widgets
from datetime import datetime
from json import dumps


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial


templater = get_renderer('homepage')

RENTAL_CART_KEY = 'rental_cart'

###################################################################
##### View shopping cart
@view_function
def process_request(request):
    params = {}

    # ensures agent has a retnal cart in the session even if they haven't added any rental products to the cart yet
    if RENTAL_CART_KEY not in request.session:
        request.session[RENTAL_CART_KEY] = []

    # 'rental_cart' is the key in this dictionary with values waiting to be assigned
    # the value of the 'rental_cart' key is a list
    params[RENTAL_CART_KEY] = []

    # rental cart is a list of rental product ID's
    for rental_product_id in request.session[RENTAL_CART_KEY]:
        # get rental product object from the rental product ID
        try:
            rental_product = hmod.RentalProduct.objects.get(id=rental_product_id)
        except hmod.Product.DoesNotExist:
            return HttpResponseRedirect('/homepage/index')

        params[RENTAL_CART_KEY].append(rental_product)

    return templater.render_to_response(request, 'rental_cart.html', params)


###################################################################
##### Add items to the rental cart
@view_function
def add(request):
    rental_product_id = request.urlparams[0]

    # ensure we have a rental cart in the session
    if RENTAL_CART_KEY not in request.session:
        request.session[RENTAL_CART_KEY] = []

    # add rental product object to rental cart
    if rental_product_id not in request.session[RENTAL_CART_KEY]:
        request.session[RENTAL_CART_KEY].append(rental_product_id)
    # else:
    # mbox.showinfo(message='This item is already in your rental shopping cart.')

    request.session.modified = True

    return HttpResponseRedirect('/homepage/rental_cart/')


###################################################################
##### Remove an item from the rental cart
@view_function
def remove(request):
    rental_pid = request.urlparams[0]

    request.session[RENTAL_CART_KEY].remove(rental_pid)
    request.session.modified = True

    return HttpResponseRedirect('/homepage/rental_cart/')


###################################################################
##### Checks username validity and stores it
@view_function
def enter_username(request):
    params = {}

    form = UsernameForm(initial={
        'discount': 0,
    })

    if request.method == 'POST':
        form = UsernameForm(request.POST)  # redisplays page with posted information

        if form.is_valid():
            due_date = form.cleaned_data['date_due']
            due_date = dumps(due_date, default=json_serial)

            request.session['username'] = form.cleaned_data['username']
            request.session['date_due'] = due_date
            request.session['discount'] = form.cleaned_data['discount']
            request.session.modified = True

            return HttpResponseRedirect('/homepage/rental_checkout/')
            # return HttpResponse('''
            #     <script>
            #         window.location.href = "/homepage/rental_checkout/";
            #     </script>
            # ''')

    params['form'] = form

    return templater.render_to_response(request, 'username.html', params)


class UsernameForm(forms.Form):
    this_year = datetime.now().year

    username = forms.CharField()
    date_due = forms.DateTimeField(label="Date Due", widget=forms.extras.widgets.SelectDateWidget(years=range(this_year, this_year + 2)))
    discount = forms.IntegerField(max_value=100, min_value=0)

    def clean(self):
        site_users_count = hmod.SiteUser.objects.filter(username=self.cleaned_data['username']).count()

        if site_users_count == 0:
            raise forms.ValidationError('This username is not associated with any accounts.')

        if self.cleaned_data['date_due'] <= datetime.now():
            raise forms.ValidationError('Please enter a due date after today.')

        return self.cleaned_data

