from django.http import Http404, HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required
from django.forms.extras import widgets
from django.utils import timezone
from django.core.mail import send_mail
import requests
from homepage.customform import CustomForm
from decimal import Decimal

templater = get_renderer('catalog')

SHIPPING_ADDRESS_KEY = 'shipping_address'
SHOPPING_CART_KEY = 'shopping_cart'

###################################################################
##### Form w/ Shipping Information

# on shipping form, have checkbox to see if the billing address is the same. If it is the same, we can populate the
# billing address form on the next page with the user's same address info
class ShippingForm(forms.Form):
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

    MOBILE = 'mobile'
    HOME = 'home'
    WORK = 'work'
    OFFICE = 'office'

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

    PHONE_TYPE_CHOICES = (
        (MOBILE, 'Mobile'),
        (HOME, 'Home'),
        (WORK, 'Work'),
        (OFFICE, 'Office'),
    )

    ship_to_new = forms.BooleanField(required=False, label="Ship to New Address")
    address1 = forms.CharField(label="Address 1*", max_length=200)
    address2 = forms.CharField(label="Address 2", max_length=200, required=False, help_text="e.g., APT #, Ste")
    city = forms.CharField(label="City*", max_length=100)
    state = forms.ChoiceField(label='State*', widget=forms.Select, choices=STATE_CHOICES)
    zip_code = forms.CharField(label='ZIP*', max_length=20)
    country = forms.CharField(label='Country*', max_length=50, required=False)
    number = forms.CharField(label="Phone", help_text="e.g., xxx-xxx-xxxx")
    phone_type = forms.ChoiceField(widget=forms.Select, choices=PHONE_TYPE_CHOICES)


###################################################################
##### Form w/ Billing Information

class BillingForm(CustomForm):
    this_year = timezone.now().year

    JAN = '01'
    FEB = '02'
    MAR = '03'
    APR = '04'
    MAY = '05'
    JUNE = '06'
    JULY = '07'
    AUG = '08'
    SEP = '09'
    OCT = '10'
    NOV = '11'
    DEC = '12'

    VISA = 'Visa'
    MASTER = 'MasterCard'
    DISCOVER = 'Discover'
    AMEX = 'AmEx'

    MONTH_CHOICES = (
        (JAN, 'Jan'),
        (FEB, 'Feb'),
        (MAR, 'Mar'),
        (APR, 'Apr'),
        (MAY, 'May'),
        (JUNE, 'June'),
        (JULY, 'July'),
        (AUG, 'Aug'),
        (SEP, 'Sep'),
        (OCT, 'Oct'),
        (NOV, 'Nov'),
        (DEC, 'Dec'),
    )

    TYPE_CHOICES = (
        (VISA, 'Visa'),
        (MASTER, 'MasterCard'),
        (DISCOVER, 'Discover'),
        (AMEX, 'American Express'),
    )

    same_as_ship = forms.BooleanField(required=False, label="Billing address same as shipping address")
    name = forms.CharField(help_text="Full name as it appears on card.")
    credit_card_no = forms.CharField(label="Credit Card Number", max_length=200)
    cvc = forms.IntegerField(label="CVC")
    card_type = forms.ChoiceField(label="Card Type", choices=TYPE_CHOICES, widget=forms.RadioSelect, initial=VISA)
    exp_month = forms.ChoiceField(label="Exp. Month", choices=MONTH_CHOICES, widget=forms.Select)
    exp_year = forms.ChoiceField(label="Exp. Year", choices=[(x, x) for x in range(this_year, this_year + 10)])

    def clean(self):
        #charge credit card with REST API call
        API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
        API_KEY = 'f65399c84d45a5039735fb33fb05d3c9'

        if self.is_valid():
            exp_year = str(self.cleaned_data['exp_year'])
            exp_year = exp_year[-2:]  #gets the last two characters of the string starting from the end

            r = requests.post(API_URL, data={
                'apiKey': API_KEY,  #API key is needed for all REST requests to our endpoint
                'currency': 'usd',  #Currency must be US dollars
                'amount': self.request.session['transaction_total'],  #Amount to the exact penny
                'type': self.cleaned_data['card_type'],  #Credit card type (Visa, MasterCard, AmEx, etc.)
                'number': self.cleaned_data['credit_card_no'],
                #Credit card number (should have already passed Luhn test)
                'exp_month': self.cleaned_data['exp_month'],  #Two-digit expiration month, left padded with 0 if needed
                'exp_year': exp_year,  #Last two digits of card expiration year
                'cvc': self.cleaned_data['cvc'],  #Standard verification code
                'name': self.cleaned_data['name'],  #Full name as it appears on the card (for verification)
                'description': 'Charge for cosmo@is411.byu.edu'
            })

            print(r.text)
            resp = r.json()

            if 'error' in resp:
                raise forms.ValidationError("ERROR: " + resp['error'])
            else:
                self.request.session['charge_resp'] = resp

        return self.cleaned_data


@view_function
def process_request(request):
    params = {}
    # email_params = {}
    # email_params['shopping_cart'] = {}
    params['user'] = request.user
    # email_params['charge_resp'] = request.session['charge_resp']
    #
    # # a key in the shopping cart is the product ID. With the key, I can query for the product object itself
    # for key in request.session[SHOPPING_CART_KEY]:
    #     try:
    #         product = hmod.Product.objects.get(id=key)
    #     except hmod.Product.DoesNotExist:
    #         return HttpResponseRedirect('/catalog/index')
    #
    #     qty = request.session[SHOPPING_CART_KEY][key]
    #
    #     email_params['shopping_cart'][product] = qty
    #
    # email_body = templater.render(request, 'purchase_receipt.html', email_params)
    #
    # subject = 'Colonial Heritage Foundation Receipt'
    # from_email = 'nate8etan@gmail.com'
    # recipient_list = ['nate8etan@gmail.com']
    #
    # send_mail(subject, email_body, from_email, recipient_list, html_message=email_body, fail_silently=False)

    return templater.render_to_response(request, 'purchase_order_confirmation.html', params)


###################################################################
##### View shopping cart
@view_function
def receipt(request):
    email_params = {}

    email_params['shopping_cart'] = {}
    email_params['user'] = request.user
    email_params['charge_resp'] = request.session['charge_resp']

    # a key in the shopping cart is the product ID. With the key, I can query for the product object itself
    for key in request.session[SHOPPING_CART_KEY]:
        try:
            product = hmod.Product.objects.get(id=key)
        except hmod.Product.DoesNotExist:
            return HttpResponseRedirect('/catalog/index')

        qty = request.session[SHOPPING_CART_KEY][key]

        email_params[SHOPPING_CART_KEY][product] = qty

    email_body = templater.render(request, 'purchase_receipt.html', email_params)

    subject = 'Colonial Heritage Foundation Purchase Receipt'
    from_email = 'nate8etan@gmail.com'
    recipient_list = ['nate8etan@gmail.com']

    send_mail(subject, email_body, from_email, recipient_list, html_message=email_body, fail_silently=False)

    # delete the shopping cart session for the user so they can continue shopping with an empty cart
    # only delete after cart has been used to create transaction
    del request.session[SHOPPING_CART_KEY]
    del request.session['transaction_total']
    del request.session['charge_resp']
    request.session.modified = True

    return HttpResponseRedirect('/catalog/checkout/')


###################################################################
##### User enters their shipping information

@view_function
def shipping(request):
    params = {}


    #########################################################################
    ##### Calculate transaction total based on info in the shopping cart and store that total in the session

    #if transaction total is not a decimal it can't compute as a float (transaction total) with a decimal (product price) and string (quantity)
    transaction_total = Decimal('0')
    for key in request.session[SHOPPING_CART_KEY]:
        try:
            product = hmod.Product.objects.get(id=key)
        except hmod.Product.DoesNotExist:
            return HttpResponseRedirect('/catalog/index')

        qty = request.session[SHOPPING_CART_KEY][key]
        transaction_total += product.product_specification.price * qty

    #if I don't cast the transaction total as a str I get a JSON not serializable error
    request.session['transaction_total'] = str(transaction_total)

    #########################################################################
    ##### Get all the info we need from the user about their addresses and phones
    site_user = request.user
    user_address_count = site_user.user_addresses.count()
    user_addresses = site_user.user_addresses.all()  #store in a list variable to access/iterate through later
    user_phone_count = site_user.user_phones.count()
    user_phones = site_user.user_phones.all()

    #########################################################################
    ##### Determine what shipping address and phone number to put in the form

    #if the user already has an address on file, then populate the form with that information, if create a blank address form
    #   for them, ready to edit
    if user_address_count == 0 and user_phone_count == 0:  #if the user doesn't have an address or a phone on file
        shipping_form = ShippingForm(initial={
            'country': 'United States',
            'phone_type': 'mobile',
        })
    elif user_phone_count == 0:  #if the user has an address on file, but not a phone
        address = user_addresses[0]
        shipping_form = ShippingForm(initial={
            'address1': address.address1,
            'address2': address.address2,
            'city': address.city,
            'state': address.state,
            'zip_code': address.zip_code,
            'country': address.country,
            'phone_type': 'mobile',
        })
    elif user_address_count == 0:  #if the user has a phone on file, but not an address
        phone = user_phones[0]
        shipping_form = ShippingForm(initial={
            'country': 'United States',
            'number': phone.number,
            'phone_type': phone.type,
        })
    else:  #if the user has both a phone and an address on file
        # return HttpResponseRedirect('/catalog/shipping/{}/{}/{}/'.format(site_user.id, user_addresses[0].id, user_phones[0].id))
        address = user_addresses[0]
        phone = user_phones[0]
        shipping_form = ShippingForm(initial={
            'address1': address.address1,
            'address2': address.address2,
            'city': address.city,
            'state': address.state,
            'zip_code': address.zip_code,
            'country': address.country,
            'number': phone.number,
            'phone_type': phone.type,
        })

    billing_form = BillingForm(request)

    if request.method == 'POST':
        shipping_form = ShippingForm(request.POST)  #redisplays page with posted information
        billing_form = BillingForm(request, request.POST)

        #shipping information will be validated before billing information so the card will only be charged once
        if shipping_form.is_valid():
            address1 = shipping_form.cleaned_data['address1']
            address2 = shipping_form.cleaned_data['address2']
            city = shipping_form.cleaned_data['city']
            state = shipping_form.cleaned_data['state']
            zip_code = shipping_form.cleaned_data['zip_code']
            country = shipping_form.cleaned_data['country']
            number = shipping_form.cleaned_data['number']
            phone_type = shipping_form.cleaned_data['phone_type']

            if billing_form.is_valid():  #if charge is successful (determined in the clean method)

                #########################################################################
                ##### Create transaction with all necessary line items associated with it

                t = hmod.Transaction()
                t.credit_card_charge_ID = request.session['charge_resp']['ID']
                t.customer = site_user
                t.save()

                #create SaleItems for all items in shopping cart
                for key in request.session[SHOPPING_CART_KEY]:
                    try:
                        product = hmod.Product.objects.get(id=key)
                    except hmod.Product.DoesNotExist:
                        return HttpResponseRedirect('/catalog/index')

                    qty = request.session[SHOPPING_CART_KEY][key]

                    sale_item = hmod.SaleItem()
                    sale_item.product = product
                    sale_item.quantity = qty
                    sale_item.calc_amount()
                    sale_item.transaction = t
                    sale_item.save()

                t.calc_sale_total()
                t.save()

                #########################################################################
                ##### Create/update address and phone based on what user wants to do

                #if the user wants to ship to a completely new address even if they already have one on file
                if shipping_form.cleaned_data['ship_to_new'] == True:
                    new_address = hmod.Address()
                    new_address.address1 = address1
                    new_address.address2 = address2
                    new_address.city = city
                    new_address.state = state
                    new_address.zip_code = zip_code
                    new_address.country = country

                    #if the user wants to ship to a new address, but doesn't even have one on file associated with them,
                    #   then we'll associate the address they just created to them
                    if user_address_count == 0:
                        new_address.user = site_user
                    new_address.save()

                    t.ships_to = new_address
                    t.save()
                #if the user doesn't have any addresses on file then create one and assign it to the transaction
                elif user_address_count == 0:
                    new_address = hmod.Address()
                    new_address.address1 = address1
                    new_address.address2 = address2
                    new_address.city = city
                    new_address.state = state
                    new_address.zip_code = zip_code
                    new_address.country = country
                    new_address.user = site_user
                    new_address.save()

                    t.ships_to = new_address
                    t.save()
                #if the user does have an address on file then save any changes and assign it to the transaction
                else:
                    address = user_addresses[0]
                    address.address1 = address1
                    address.address2 = address2
                    address.city = city
                    address.state = state
                    address.zip_code = zip_code
                    address.country = country
                    address.save()

                    t.ships_to = address
                    t.save()

                #if the user doesn't have any phones on file, then create one and assign it to the user
                if user_phone_count == 0:
                    new_phone = hmod.Phone()
                    new_phone.number = number
                    new_phone.type = phone_type
                    new_phone.user = site_user
                    new_phone.save()

                #if the user does have a phone on file, then update it
                else:
                    phone = user_phones[0]
                    phone.number = number
                    phone.type = phone_type
                    phone.save()

                return HttpResponseRedirect('/catalog/receipt/')

    params['shipping_form'] = shipping_form
    params['billing_form'] = billing_form

    return templater.render_to_response(request, 'shipping2.html', params)