from django.http import Http404, HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required
from datetime import datetime
from decimal import Decimal
from django.template.defaultfilters import floatformat
from homepage.customform import CustomForm
import requests

templater = get_renderer('homepage')

RENTAL_RETURN_ITEMS_KEY = 'rental_return_items'
DAMAGE_KEY = 'damage'
LATE_FEE_MULTIPLIER = 1.5


###################################################################
##### Find the customer with their username
@view_function
def process_request(request):
    params = {}

    form = UsernameForm()

    if request.method == 'POST':
        form = UsernameForm(request.POST)  # redisplays page with posted information

        if form.is_valid():
            username = form.cleaned_data['username']
            request.session['rental_username'] = username

            return HttpResponseRedirect('/homepage/rental_return.rental_items')

    params['form'] = form

    return templater.render_to_response(request, 'rental_username.html', params)


@view_function
def update_session(request):
    today = datetime.now()
    rental_item_id_str = request.REQUEST.get('line_item_id')
    damage_fee_str = request.REQUEST.get('fee')
    damage_desc = request.REQUEST.get('desc')

    rental_item_id_int = int(rental_item_id_str)

    # if isinstance(rental_item_id_int, int):
    # print("rental_item_id_int is a int.")
    # else:
    # print("rental_item_id_int is NOT a int.")

    try:
        rental_item = hmod.RentalItem.objects.get(id=rental_item_id_int)
    except hmod.RentalItem.DoesNotExist:
        return HttpResponse('No')

    if DAMAGE_KEY not in request.session:
        request.session[DAMAGE_KEY] = {}

    if today >= rental_item.date_due:
        days_overdue_timedelta = today - rental_item.date_due
        # float cannot be multiplied by Decimals
        late_fee_price_per_day_decimal = Decimal(LATE_FEE_MULTIPLIER) * rental_item.rental_product.price_per_day
        # converting late_fee_price_per_day_decimal to a SafeText str so that it will only have two decimals
        late_fee_price_per_day_str = floatformat(late_fee_price_per_day_decimal, 2)

        # convert late_fee_price_per_day_str back to a Decimal for calculations
        late_fee_amount_decimal = days_overdue_timedelta.days * Decimal(late_fee_price_per_day_str)
        late_fee_amount_decimal_str = floatformat(late_fee_amount_decimal, 2)
    else:
        late_fee_amount_decimal_str = '0'

    request.session[DAMAGE_KEY][rental_item_id_int] = [late_fee_amount_decimal_str, damage_fee_str, damage_desc]
    # print("Rental Item ID: %s" % request.session[DAMAGE_KEY])

    # del request.session[DAMAGE_KEY]
    request.session.modified = True

    return HttpResponse('Success!')


@view_function
def rental_items(request):
    params = {}

    if RENTAL_RETURN_ITEMS_KEY not in request.session:
        request.session[RENTAL_RETURN_ITEMS_KEY] = []
    # get the customer and all of their unreturned rental items
    try:
        customer = hmod.SiteUser.objects.get(username=request.session['rental_username'])
    except hmod.SiteUser.DoesNotExist:
        return HttpResponseRedirect('/homepage/rental_return')

    rental_item_list = hmod.RentalItem.objects.filter(transaction__customer=customer, date_in=None)

    trans_dict = {}
    if rental_item_list != []:
        for rental_item in rental_item_list:
            request.session[RENTAL_RETURN_ITEMS_KEY].append(rental_item.id)

            # create a unique dict of transactions for the customer and the rental items of that transaction
            rental_item_trans = rental_item.transaction
            if rental_item_trans not in trans_dict:
                trans_dict[rental_item_trans] = hmod.RentalItem.objects.filter(transaction=rental_item_trans)

    request.session.modified = True
    params['customer'] = customer
    params['rental_items'] = trans_dict

    return templater.render_to_response(request, 'rental_items.html', params)


@view_function
def summary(request):
    params = {}
    params['rental_items'] = {}
    today = datetime.now()

    try:
        customer = hmod.SiteUser.objects.get(username=request.session['rental_username'])
    except hmod.SiteUser.DoesNotExist:
        return HttpResponseRedirect('/homepage/rental_return')

    late_fee_total_decimal = Decimal('0')
    damage_fee_total_decimal = Decimal('0')

    rental_item_dict = {}
    for rental_item_id in request.session[DAMAGE_KEY]:
        try:
            rental_item = hmod.RentalItem.objects.get(id=rental_item_id)
        except hmod.SiteUser.DoesNotExist:
            return HttpResponseRedirect('/homepage/rental_return')

        rental_item_dict[rental_item] = []

        late_fee_str = request.session[DAMAGE_KEY][rental_item_id][0]
        damage_fee_str = request.session[DAMAGE_KEY][rental_item_id][1]

        if late_fee_str != '':
            late_fee_total_decimal += Decimal(late_fee_str)

        if damage_fee_str != '':
            damage_fee_total_decimal += Decimal(damage_fee_str)

        rental_item_dict[rental_item].append(late_fee_str)
        rental_item_dict[rental_item].append(damage_fee_str)
        rental_item_dict[rental_item].append(request.session[DAMAGE_KEY][rental_item_id][2])

    fee_total_decimal = late_fee_total_decimal + damage_fee_total_decimal
    request.session['fee_total'] = floatformat(fee_total_decimal, 2)
    # request.session['damage_fee_total'] = damage_fee_total_decimal
    request.session.modified = True

    form = BillingForm(request, initial={
        'name': 'Cosmo Limesandal',
        'credit_card_no': '4732817300654',
        'cvc': '411',
        'exp_month': '10',
        'exp_year': '2015'
    })

    if request.method == 'POST':
        form = BillingForm(request, request.POST)

        if form.is_valid():
            agent = request.user

            try:
                emp = hmod.Employee.objects.get(id=agent.person.id)
            except hmod.Employee.DoesNotExist:
                return HttpResponseRedirect('/homepage/index/')

            if fee_total_decimal != 0:
                t = hmod.Transaction()
                t.credit_card_charge_ID = request.session['return_charge_resp']['ID']
                t.customer = customer
                t.handled_by = emp
                t.save()

                for rental_item in rental_item_dict:
                    if rental_item_dict[rental_item][0] != '':
                        late_fee = hmod.LateFee()
                        late_fee.transaction = t
                        late_fee.rental_item = rental_item
                        late_fee.calc_amount()  # sets the days_late and the amount attributes
                        late_fee.save()

                    if rental_item_dict[rental_item][1] != '':
                        damage_fee = hmod.DamageFee()
                        damage_fee.amount = Decimal(rental_item_dict[rental_item][1])
                        damage_fee.transaction = t
                        damage_fee.rental_item = rental_item
                        damage_fee.description = rental_item_dict[rental_item][2]
                        damage_fee.save()

            for rental_item in rental_item_dict:
                rental_item.date_in = today
                rental_item.save()

            return HttpResponseRedirect('/homepage/rental_return.thank_you')

    params['form'] = form
    params['rental_items'] = rental_item_dict
    params['late_fee_total'] = floatformat(late_fee_total_decimal, 2)
    params['damage_fee_total'] = floatformat(damage_fee_total_decimal, 2)
    params['customer'] = customer

    return templater.render_to_response(request, 'return_summary.html', params)


@view_function
def thank_you(request):
    params = {}

    try:
        user = hmod.SiteUser.objects.get(username=request.session['rental_username'])
    except hmod.SiteUser.DoesNotExist:
        return HttpResponseRedirect('/homepage/index/')

    params['user'] = user

    del request.session['rental_username']
    request.session.modified = True

    return templater.render_to_response(request, 'thank_you.html', params)


class UsernameForm(forms.Form):
    username = forms.CharField(label='Enter Username')

    def clean_username(self):
        site_users_count = hmod.SiteUser.objects.filter(username=self.cleaned_data['username']).count()

        if site_users_count == 0:
            raise forms.ValidationError('This username is not associated with any accounts.')

        return self.cleaned_data['username']


###################################################################
##### Form w/ Billing Information

class BillingForm(CustomForm):
    this_year = datetime.now().year

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
            if self.request.session['fee_total'] != 0:
                exp_year = str(self.cleaned_data['exp_year'])
                exp_year = exp_year[-2:]  # gets the last two characters of the string starting from the end

                r = requests.post(API_URL, data={
                    'apiKey': API_KEY,  # API key is needed for all REST requests to our endpoint
                    'currency': 'usd',  #Currency must be US dollars
                    'amount': self.request.session['fee_total'],  #Amount to the exact penny
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
                    self.request.session['return_charge_resp'] = resp

        return self.cleaned_data
