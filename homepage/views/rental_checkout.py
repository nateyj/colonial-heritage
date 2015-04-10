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
from decimal import *
from datetime import datetime, timedelta
from django.template.defaultfilters import floatformat

templater = get_renderer('homepage')

RENTAL_CART_KEY = 'rental_cart'

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
        # charge credit card with REST API call
        API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
        API_KEY = 'f65399c84d45a5039735fb33fb05d3c9'

        if self.is_valid():
            if self.request.session['discount'] != 100:
                exp_year = str(self.cleaned_data['exp_year'])
                exp_year = exp_year[-2:]  #gets the last two characters of the string starting from the end

                r = requests.post(API_URL, data={
                    'apiKey': API_KEY,  #API key is needed for all REST requests to our endpoint
                    'currency': 'usd',  #Currency must be US dollars
                    'amount': self.request.session['rental_transaction_total'],  #Amount to the exact penny
                    'type': self.cleaned_data['card_type'],  #Credit card type (Visa, MasterCard, AmEx, etc.)
                    'number': self.cleaned_data['credit_card_no'],
                    #Credit card number (should have already passed Luhn test)
                    'exp_month': self.cleaned_data['exp_month'],
                    #Two-digit expiration month, left padded with 0 if needed
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
                    # print(resp.keys())
                    self.request.session['rental_charge_resp'] = resp

        return self.cleaned_data


@view_function
def order_confirmation(request):
    params = {}

    try:
        user = hmod.SiteUser.objects.get(username=request.urlparams[0])
    except hmod.SiteUser.DoesNotExist:
        return HttpResponseRedirect('/homepage/index/')

    params['user'] = user

    return templater.render_to_response(request, 'rental_order_confirmation.html', params)


###################################################################
#####
@view_function
def receipt(request):
    email_params = {}
    username = request.session['username']
    discount = request.session['discount']

    email_params[RENTAL_CART_KEY] = []

    if discount != 100:
        email_params['rental_charge_resp'] = request.session['rental_charge_resp']

    try:
        user = hmod.SiteUser.objects.get(username=username)
    except hmod.SiteUser.DoesNotExist:
        return HttpResponseRedirect('/homepage/index/')

    email_params['user'] = user

    try:
        if discount != 100:
            trans = hmod.Transaction.objects.get(credit_card_charge_ID=request.session['rental_charge_resp']['ID'])
        else:
            trans = hmod.Transaction.objects.get(credit_card_charge_ID='free', customer=user)
    except hmod.Transaction.DoesNotExist:
        return HttpResponseRedirect('/homepage/index/')

    rental_item_list = hmod.RentalItem.objects.filter(transaction=trans)

    for item in rental_item_list:
        email_params[RENTAL_CART_KEY].append(item)
        email_params['date_due'] = item.date_due

    email_params['transaction'] = trans

    email_body = templater.render(request, 'rental_receipt.html', email_params)

    subject = 'Colonial Heritage Foundation Rental Receipt'
    from_email = 'isgroup2.9@gmail.com'
    recipient_list = ['nate8etan@gmail.com']

    send_mail(subject, email_body, from_email, recipient_list, html_message=email_body, fail_silently=False)

    # delete the rental cart session for the agent so they can continue shopping with an empty cart
    # only delete after cart has been used to create transaction
    del request.session[RENTAL_CART_KEY]
    del request.session['username']
    del request.session['discount']
    del request.session['rental_days']
    del request.session['rental_transaction_total']
    del request.session['date_due']

    if discount != 100:
        del request.session['rental_charge_resp']

    request.session.modified = True

    return HttpResponseRedirect('/homepage/rental_checkout.order_confirmation/{}'.format(username))


###################################################################
##### User enters their billing information
@view_function
def process_request(request):
    params = {}
    params['rental_cart'] = {}

    # getcontext().prec = 4
    #########################################################################
    ##### Calculate transaction total based on info in the rental cart and store that total in the session
    today = datetime.now()
    print("Today: {}".format(today))
    print("Today's Day: {}".format(today.day))
    due_date_datetime = datetime.strptime(request.session['date_due'], '"%Y-%m-%dT%H:%M:%S"')
    # if isinstance(due_date, datetime):
    # print("due_date is a datetime.")
    # else:
    #     print("due_date is NOT a datetime.")
    print("Due Date: {}".format(due_date_datetime))
    print("Due Date's Day: {}".format(due_date_datetime.day))

    discount_int = request.session['discount']
    # if isinstance(discount, int):
    #     print("discount is an int.")
    # else:
    #     print("discount is NOT an int.")

    rental_days_timedelta = due_date_datetime - today
    rental_days_int = due_date_datetime.day - today.day
    # print("Rental Days in rental_checkout: {}".format(rental_days_timedelta.days))
    print("Rental Days in rental_checkout: {}".format(rental_days_int))
    # rental_days_int = rental_days_timedelta.days + 2


    # if isinstance(rental_days_timedelta.days, int):
    #     print("rental_days_timedelta.days is an int.")
    # else:
    #     print("rental_days_timedelta.days is NOT an int.")
    print("Rental Days: %d" % rental_days_int)
    ################################# timedelta.days is an int
    request.session['rental_days'] = rental_days_int

    #if transaction total is not a decimal it can't compute as a float (transaction total) with a decimal (product price) and string (quantity)
    transaction_subtotal_decimal = Decimal('0')
    rental_product_list = []
    for rental_pid in request.session[RENTAL_CART_KEY]:
        try:
            rental_product = hmod.RentalProduct.objects.get(id=rental_pid)
        except hmod.RentalProduct.DoesNotExist:
            return HttpResponseRedirect('/homepage/rental_products')
        # calculate subtotal for each rental product by multiplying the days rented by the price per day
        rental_item_subtotal_decimal = rental_product.price_per_day * rental_days_int
        # if isinstance(rental_item_subtotal, Decimal):
        #     print("rental_item_subtotal is a Decimal.")
        # else:
        #     print("rental_item_subtotal is NOT a Decimal.")
        rental_item_subtotal_str = floatformat(rental_item_subtotal_decimal, 2)
        print('%s: $%s' % (rental_product.product_specification.name, rental_item_subtotal_str))
        params['rental_cart'][rental_product] = rental_item_subtotal_str

        # calculate rental total by adding each subtotal to the total
        transaction_subtotal_decimal += Decimal(rental_item_subtotal_str)
        print('Transaction Subtotal: $%d' % transaction_subtotal_decimal)
        #add rental products to a list
        rental_product_list.append(rental_product)

    params['transaction_subtotal'] = floatformat(transaction_subtotal_decimal, 2)
    print("Discount: %d" % discount_int)
    discount_float = discount_int / 100
    print("Discount Float: %f" % discount_float)

    # Decimal(discount_float) will be a Decimal object
    transaction_total_decimal = transaction_subtotal_decimal * (1 - Decimal(discount_float))
    transaction_total_str = floatformat(transaction_total_decimal, 2)
    # if isinstance(transaction_total, Decimal):
    #     print("transaction_total is a Decimal.")
    # else:
    #     print("transaction_total is NOT a Decimal.")
    print('Transaction Total: $%s' % transaction_total_str)

    #if I don't cast the transaction total as a str I get a JSON not serializable error
    request.session['rental_transaction_total'] = transaction_total_str
    request.session.modified = True

    #########################################################################
    ##### Get the user from the username stored in the session
    try:
        customer = hmod.SiteUser.objects.get(username=request.session['username'])
    except hmod.SiteUser.DoesNotExist:
        return HttpResponseRedirect('/homepage/rental_products')

    # form = BillingForm(request, initial={
    #     'name': 'Cosmo Limesandal',
    #     'credit_card_no': '4732817300654',
    #     'cvc': '411',
    #     'exp_month': '10',
    #     'exp_year': '2015'
    # })

    form = BillingForm(request)

    if request.method == 'POST':
        form = BillingForm(request, request.POST)

        if form.is_valid():  #if charge is successful (determined in the clean method)
            agent = request.user

            try:
                emp = hmod.Employee.objects.get(id=agent.person.id)
            except hmod.Employee.DoesNotExist:
                return HttpResponseRedirect('/homepage/index/')
            #########################################################################
            ##### Create transaction with all necessary line items associated with it
            t = hmod.Transaction()

            if request.session['discount'] != 100:
                t.credit_card_charge_ID = request.session['rental_charge_resp']['ID']
            else:
                t.credit_card_charge_ID = 'free'

            t.customer = customer
            t.checked_out_by = emp
            t.save()

            #create RentalItems for all items in rental cart
            for rental_product in rental_product_list:
                rental_product.times_rented += 1

                rental_item = hmod.RentalItem()
                rental_item.rental_product = rental_product
                rental_item.date_due = due_date_datetime
                rental_item.discount_percent = discount_int
                rental_item.transaction = t
                rental_item.save()  #at this time, the date_out is set and the amount & pre_discount_amount = 0

                rental_item.calc_amount()  #can't call it earlier because there's no date_out
                rental_item.save()

            t.calc_pre_discount_rental_total()
            t.calc_rental_total()
            t.save()

            return HttpResponseRedirect('/homepage/rental_checkout.receipt/')

    params['form'] = form
    params['date_due'] = due_date_datetime
    params['discount'] = discount_int

    return templater.render_to_response(request, 'rental_checkout.html', params)