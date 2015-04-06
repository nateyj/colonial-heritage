from django.http import Http404, HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from homepage.customform import CustomForm
from django.contrib.auth.decorators import permission_required
from datetime import datetime, timedelta
from django.core.mail import send_mail
from decimal import Decimal
from django.template.defaultfilters import floatformat

templater = get_renderer('homepage')

LATE_FEE_MULTIPLIER = 1.5
OVERDUE_ITEMS_KEY = 'overdue_items'

#########################################################################
### View list of all items overdue

@view_function
def overdue_email(request):
    email_params = {}

    subject = 'Overdue Rental Items Reminder'
    from_email = 'nate8etan@gmail.com'
    today = datetime.now()

    # query to find all objects overdue
    # make sure that it only pulls rental items that haven't been checked in already
    rental_items_list = hmod.RentalItem.objects.filter(date_due__lte=today, date_in=None)

    users_list = []

    # create a unique list of users that have rental items overdue
    for rental_item in rental_items_list:
        if rental_item.transaction.customer in users_list:
            continue

        users_list.append(rental_item.transaction.customer)

    # iterate through users and send them an email if they rental items due
    for user in users_list:
        # creates a list of transactions that contain rental items that have not been returned and are overdue

        # store user in params to be able to display their name in the email
        email_params['user'] = user
        print("User: {}".format(user))
        # get a list of all of the user's transactions
        user_transactions_list = user.transactions.all()

        # initialize/reset dictionary that holds all of the user's overdue items for each user
        email_params[OVERDUE_ITEMS_KEY] = {}
        for trans in user_transactions_list:
            print("Transaction: {}".format(trans))
            # get a list of rental items that are associated with a user's transaction AND haven't been returned yet
            #   This will look over other rental transactions the user has made where they have returned the items
            rental_items_in_trans = hmod.RentalItem.objects.filter(transaction=trans, date_in=None)

            # if the list of rental items is actually populated with unreturned rental items
            if rental_items_in_trans != []:
                for item in rental_items_in_trans:
                    print("Item: {}".format(item))
                    # don't need to check if the item is already in the overdue_items key, because a rental item can't
                    #   be rented again until it is checked in, so they will always be unique, but we will for good measure
                    if item not in email_params[OVERDUE_ITEMS_KEY]:
                        email_params[OVERDUE_ITEMS_KEY][item] = []

                        days_overdue_timedelta = today - item.date_due
                        # float cannot be multiplied by Decimals
                        late_fee_price_per_day_decimal = Decimal(
                            LATE_FEE_MULTIPLIER) * item.rental_product.price_per_day
                        # converting late_fee_price_per_day_decimal to a SafeText str so that it will only have two decimals
                        late_fee_price_per_day_str = floatformat(late_fee_price_per_day_decimal, 2)

                        # convert late_fee_price_per_day_str back to a Decimal for calculations
                        late_fee_amount_decimal = days_overdue_timedelta.days * Decimal(late_fee_price_per_day_str)
                        late_fee_amount_decimal_str = floatformat(late_fee_amount_decimal, 2)

                        email_params[OVERDUE_ITEMS_KEY][item].append(late_fee_price_per_day_str)
                        email_params[OVERDUE_ITEMS_KEY][item].append(late_fee_amount_decimal_str)
                        email_params[OVERDUE_ITEMS_KEY][item].append(trans)

        if days_overdue_timedelta is not None:
            email_params['days_overdue'] = days_overdue_timedelta.days

        email_body = templater.render(request, 'overdue_reminder.html', email_params)

        # recipient_list = [user.email]
        recipient_list = ['nate8etan@gmail.com']

        # for testing purposes
        # return templater.render_to_response(request, 'overdue_reminder.html', email_params)

        send_mail(subject, email_body, from_email, recipient_list, html_message=email_body, fail_silently=False)

    return HttpResponseRedirect('/homepage/')


@view_function
def process_request(request):
    params = {}
    today_datetime = datetime.now()
    thirty_timedelta = today_datetime - timedelta(days=30)
    sixty_timedelta = today_datetime - timedelta(days=60)
    ninety_timedelta = today_datetime - timedelta(days=90)

    thirtyTo60_list = hmod.RentalItem.objects.filter(date_in=None, date_due__range=[sixty_timedelta, thirty_timedelta])
    sixtyTo90_list = hmod.RentalItem.objects.filter(date_in=None, date_due__range=[ninety_timedelta, sixty_timedelta])
    over90_list = hmod.RentalItem.objects.filter(date_in=None, date_due__lte=ninety_timedelta)

    # contains the customers of the rental items of the specified period, their transactions, and all rental items of
    # those transactions
    thirtyTo60_customers_dict = {}
    sixtyTo90_customers_dict = {}
    over90_customers_dict = {}

    # contains the customers of the rental items of the specified period, their transactions, and how many days the
    # transaction is overdue
    thirtyTo60_days_overdue_dict = {}
    sixtyTo90_days_overdue_dict = {}
    over90_days_overdue_dict = {}

    # create unique dicts of customes that have rental items 30-59 days overdue
    for rental_item in thirtyTo60_list:
        customer = rental_item.transaction.customer
        days_overdue_timedelta = today_datetime - rental_item.date_due
        rental_item_transaction = rental_item.transaction

        # if the customer isn't yet in the dict then add them, the transaction, and the rental item
        if customer not in thirtyTo60_customers_dict:

            # thirtyTo60_users_dict = {customer: {transaction: [rental_items]}}
            thirtyTo60_customers_dict[customer] = {rental_item_transaction: [rental_item]}

        # add the rental_item_transaction to the customer's dict and the associated rental item
        elif rental_item_transaction not in thirtyTo60_customers_dict[customer]:
            thirtyTo60_customers_dict[customer][rental_item_transaction] = [rental_item]

        # add the rental_item to the transaction's list
        else:
            thirtyTo60_customers_dict[customer][rental_item_transaction].append(rental_item)

        # if the customer isn't yet in the dict then add them, the transaction, and how many days the transaction is overdue
        if customer not in thirtyTo60_days_overdue_dict:
            thirtyTo60_days_overdue_dict[customer] = {rental_item_transaction: days_overdue_timedelta.days}

        # if the rental item's transaction is not in the dict, add the transaction and how many days it's overdue
        elif rental_item_transaction not in thirtyTo60_days_overdue_dict[customer]:
            thirtyTo60_days_overdue_dict[customer][rental_item_transaction] = days_overdue_timedelta.days

            # if the customer of the rental item and the rental item's transaction are already in thirtyTo60_days_overdue_dict,
            # then the how many days the transaction is overdue is already in the dict as well

    # create unique dicts of customers that have rental items 60-89 days overdue
    for rental_item in sixtyTo90_list:
        customer = rental_item.transaction.customer
        days_overdue_timedelta = today_datetime - rental_item.date_due
        rental_item_transaction = rental_item.transaction

        if customer not in sixtyTo90_customers_dict:
            sixtyTo90_customers_dict[customer] = {rental_item_transaction: [rental_item]}

        elif rental_item_transaction not in sixtyTo90_customers_dict[customer]:
            sixtyTo90_customers_dict[customer][rental_item_transaction] = [rental_item]

        else:
            sixtyTo90_customers_dict[customer][rental_item_transaction].append(rental_item)

        if customer not in sixtyTo90_days_overdue_dict:
            sixtyTo90_days_overdue_dict[customer] = {rental_item_transaction: days_overdue_timedelta.days}

        elif rental_item_transaction not in sixtyTo90_days_overdue_dict[customer]:
            sixtyTo90_days_overdue_dict[customer][rental_item_transaction] = days_overdue_timedelta.days

    # create unique dicts of customers that have rental items >= 90 days overdue
    for rental_item in over90_list:
        customer = rental_item.transaction.customer
        days_overdue_timedelta = today_datetime - rental_item.date_due
        rental_item_transaction = rental_item.transaction

        if customer not in over90_customers_dict:
            over90_customers_dict[customer] = {rental_item_transaction: [rental_item]}

        elif rental_item_transaction not in over90_customers_dict[customer]:
            over90_customers_dict[customer][rental_item_transaction] = [rental_item]

        else:
            over90_customers_dict[customer][rental_item_transaction].append(rental_item)

        if customer not in over90_days_overdue_dict:
            over90_days_overdue_dict[customer] = {rental_item_transaction: days_overdue_timedelta.days}

        elif rental_item_transaction not in over90_days_overdue_dict[customer]:
            over90_days_overdue_dict[customer][rental_item_transaction] = days_overdue_timedelta.days

    params['thirtyTo60_days_overdue_dict'] = thirtyTo60_days_overdue_dict
    params['thirtyTo60_customers_dict'] = thirtyTo60_customers_dict
    params['sixtyTo90_days_overdue_dict'] = sixtyTo90_days_overdue_dict
    params['sixtyTo90_customers_dict'] = sixtyTo90_customers_dict
    params['over90_days_overdue_dict'] = over90_days_overdue_dict
    params['over90_customers_dict'] = over90_customers_dict

    return templater.render_to_response(request, 'batch.html', params)