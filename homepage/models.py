from django.db import models
from django.contrib.auth.models import User, AbstractUser
import random
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.utils import timezone
from datetime import datetime
from polymorphic import PolymorphicModel
from django.contrib.auth.models import Group
from decimal import Decimal

LATE_FEE_MULTIPLIER = 1.5


class SiteUser(AbstractUser):
    # INHERITED FIELDS:
    # password
    # last_login
    # username
    # first_name
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined
    security_question = models.TextField(max_length=200, null=True, blank=True)
    security_answer = models.TextField(max_length=200, null=True, blank=True)
    # organization_name = models.TextField(max_length=200, null=True, blank=True)
    # date_appointed_agent = models.DateField(null=True)
    # bio_sketch = models.TextField(max_length=1000, null=True, blank=True)
    # emergency_contact_name = models.TextField(max_length=200, null=True, blank=True)
    # emergency_contact_phone = models.TextField(max_length=200, null=True, blank=True)
    # emergency_contact_relationship = models.TextField(max_length=200, null=True, blank=True)

    # address and phone are nullable until the user wants to buy or rent something
    # photo_id = models.ForeignKey(Photograph, related_name='+')


    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_group(self):
        users_in_admin = Group.objects.get(name="Administrator").user_set.all()
        users_in_manager = Group.objects.get(name="Manager").user_set.all()
        users_in_agent = Group.objects.get(name="Agent").user_set.all()
        users_in_guest = Group.objects.get(name="Guest").user_set.all()

        if self in users_in_admin:
            return 'Administrator'
        if self in users_in_manager:
            return 'Manager'
        if self in users_in_agent:
            return 'Agent'
        if self in users_in_guest:
            return 'Guest'

    def get_checked_out_rental_items(self):
        all_checked_out_rental_items = []
        # user_transactions is a list of transactions a user has placed
        user_transactions = self.transactions.all()

        for transaction in user_transactions:
            # unreturned_rental_items is a list of unreturned rental items for this particular transaction
            tran_checked_out_rental_items = RentalItem.objects.filter(date_in=None, transaction=transaction)

            # check to see if the unreturned_rental_items list is empty. What if the query above was querying an online sale
            #   transaction rather than a rental transaction?
            if tran_checked_out_rental_items != 0:
                #iterate through unreturned_rental_items and add each item to the params dictionary individually
                for item in tran_checked_out_rental_items:
                    all_checked_out_rental_items.append(item)

        return all_checked_out_rental_items


class Address(models.Model):
    address1 = models.TextField(max_length=200, blank=True)
    address2 = models.TextField(max_length=200, null=True, blank=True)
    city = models.TextField(max_length=100, blank=True)
    state = models.TextField(max_length=2, blank=True)
    zip_code = models.TextField(max_length=20, blank=True)
    country = models.TextField(max_length=50, blank=True, default='United States')
    user = models.ForeignKey(SiteUser, related_name='user_addresses', null=True)

    class Meta:
        ordering = ['country', 'state', 'city', 'zip_code', 'address1', 'address2']
        verbose_name_plural = 'addresses'

    def __str__(self):
        return '{} {} {}, {} {}, {}'.format(self.address1, self.address2, self.city, self.state, self.zip_code,
                                            self.country)


class Organization(PolymorphicModel):
    given_name = models.TextField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    address = models.ForeignKey(Address)

    def __str__(self):
        return '{}'.format(self.given_name)


class Phone(models.Model):
    number = models.TextField(max_length=40, blank=True)
    extension = models.PositiveSmallIntegerField(null=True)
    type = models.TextField(max_length=6)
    user = models.ForeignKey(SiteUser, related_name='user_phones', null=True)
    organization = models.ForeignKey(Organization, related_name='org_phones', null=True)

    def __str__(self):
        return '{} {}'.format(self.number, self.type)


class PublicEvent(models.Model):
    name = models.TextField(max_length=200, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class Event(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    map_file_name = models.FileField(upload_to='files/%Y/%m/%d', null=True)
    public_event = models.ForeignKey(PublicEvent, related_name='events')

    def __str__(self):
        return '{}'.format(self.public_event.name)


class Venue(models.Model):
    name = models.TextField(max_length=200, blank=True)
    address = models.OneToOneField(Address)
    venue_contact = models.ForeignKey(Phone, related_name='+', null=True)
    event = models.OneToOneField(Event, null=True)

    def __str__(self):
        return '{}'.format(self.name)


# person class exists, because there are owners of items that need to be recorded
class Person(Organization):
    # given_name
    # email
    #address
    last_name = models.TextField(max_length=50, blank=True)
    birth_date = models.DateField(null=True)
    account = models.OneToOneField(SiteUser, related_name='person',
                                   null=True)  # people don't have an account unless they become an agent or customer

    def __str__(self):
        return '{} {}'.format(self.given_name, self.last_name)


# when an agent is created, an account must also be created for them

# all participants are volunteers and all volunteers are agents. If CHF expands enough, there could be agents who are
# employees. Volunteers and Employees would sit on the same level in an inheritance tree. Staff and Performers are
# subclasses of Participant

# all participants must have a photo ID, which must be enforced on the front end since it is not here
class Participant(Person):
    #given_name
    #email
    #address
    #last_name
    #birth_date
    #account
    bio_sketch = models.TextField(max_length=1000, blank=True)
    emergency_contact_name = models.TextField(max_length=200, blank=True)
    emergency_contact_phone = models.ForeignKey(Phone)
    emergency_contact_relationship = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return '{} {}'.format(self.given_name, self.last_name)


class Employee(Person):
    #given_name
    #email
    #address
    #last_name
    #birth_date
    #account
    date_hired = models.DateField()
    wage = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return '{} {}'.format(self.given_name, self.last_name)


# class Salary(Employee):
#     salary = models.DecimalField()
#
#
# class Hourly(Employee):
#     wage = models.DecimalField()


class Area(models.Model):
    name = models.TextField(max_length=200, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    place_number = models.PositiveIntegerField()
    coordinator = models.ForeignKey(Participant, related_name='coordinates')
    supervisor = models.ForeignKey(Employee, related_name='supervises')
    public_event = models.ForeignKey(PublicEvent, related_name='areas')
    participants = models.ManyToManyField(Participant, through='ParticipantRole', null=True)

    def __str__(self):
        return '{}'.format(self.name)


class ArtisanItem(models.Model):
    name = models.TextField(max_length=200, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    area = models.ForeignKey(Area, related_name='artisan_items')

    def __str__(self):
        return '{}'.format(self.name)


class Photograph(models.Model):
    date_taken = models.DateTimeField(null=True)
    place_taken = models.TextField(max_length=200, null=True, blank=True)
    name = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='images')
    public_event = models.ForeignKey(PublicEvent, related_name='public_event_photos', null=True)
    event = models.ForeignKey(Event, related_name='event_photos', null=True)
    venue = models.ForeignKey(Venue, related_name='venue_photos', null=True)
    artisan_item = models.ForeignKey(ArtisanItem, related_name='artisan_item_photos', null=True)
    area = models.ForeignKey(Area, related_name='area_photos', null=True)
    participant = models.OneToOneField(Participant, related_name='photo_id', null=True)

    def __str__(self):
        return '{}'.format(self.name)


class ParticipantRole(models.Model):
    participant = models.ForeignKey(Participant)
    area = models.ForeignKey(Area)
    name = models.TextField(max_length=200, blank=True)
    type = models.TextField(max_length=40, blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pre_discount_total = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    # date_packed = models.DateTimeField(null=True)
    # date_paid = models.DateTimeField(null=True)
    # date_shipped = models.DateTimeField(null=True)
    # tracking_number = models.TextField(max_length=12, null=True)
    ships_to = models.ForeignKey(Address, null=True)
    credit_card_charge_ID = models.TextField(null=True)
    # packed_by = models.ForeignKey(Employee, related_name='packedby_set', null=True)
    checked_in_by = models.ForeignKey(Employee, related_name='checked_in_set', null=True)
    # shipped_by = models.ForeignKey(Employee, related_name='shippedby_set', null=True)
    checked_out_by = models.ForeignKey(Employee, related_name='checked_out_set', null=True)
    handled_by = models.ForeignKey(Employee, related_name='handledby_set', null=True)
    customer = models.ForeignKey(SiteUser, related_name='transactions')

    # add line item method possibly

    #call this method only after line items have been assigned to this transaction
    def calc_rental_total(self):
        # get all line items of this transaction
        # can't query transaction line items, because it's an abstract class
        line_items = RentalItem.objects.filter(transaction=self)

        for line_item in line_items:
            self.total += line_item.amount

    #call this method only after line items have been assigned to this transaction
    def calc_pre_discount_rental_total(self):
        # get all line items of this transaction
        # can't query transaction line items, because it's an abstract class
        line_items = RentalItem.objects.filter(transaction=self)

        for line_item in line_items:
            self.pre_discount_total += line_item.pre_discount_amount

    def calc_sale_total(self):
        # get all line items of this transaction
        # can't query transaction line items, because it's an abstract class
        line_items = SaleItem.objects.filter(transaction=self)

        for line_item in line_items:
            self.total += line_item.amount

    def get_rental_item_count(self):
        # get all line items of this transaction
        # can't query transaction line items, because it's an abstract class
        line_items = RentalItem.objects.filter(transaction=self).count()
        return line_items

    def get_sale_item_count(self):
        # get all line items of this transaction
        # can't query transaction line items, because it's an abstract class
        sale_item_count = 0
        line_items = SaleItem.objects.filter(transaction=self)

        for line_item in line_items:
            sale_item_count += line_item.quantity

        return sale_item_count


class TransactionLineItem(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 default=0)  # quantity * price of the product, product.product_specification.price
    transaction = models.ForeignKey(Transaction)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.TextField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)


class ProductSpecification(models.Model):
    name = models.TextField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    order_form_name = models.TextField(max_length=200, null=True)
    production_time = models.TextField(max_length=200, null=True)
    category = models.ForeignKey(Category, related_name='+')
    producer = models.ForeignKey(Organization, null=True)
    photo = models.OneToOneField(Photograph, null=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.price)


class Product(PolymorphicModel):
    qty_on_hand = models.PositiveIntegerField(default=1)
    shelf_location = models.TextField(max_length=40, null=True, blank=True)
    order_file = models.TextField(null=True)
    product_specification = models.ForeignKey(ProductSpecification, related_name='+')

    def __str__(self):
        return '{}'.format(self.product_specification.name)


class SerializedProduct(Product):
    # qty_on_hand must equal 1
    # shelf_location
    # order_file
    # product_specification
    serial_number = models.TextField(max_length=12, unique=True, null=True)
    date_acquired = models.DateField(auto_now_add=True)
    status = models.TextField(max_length=40, null=True, blank=True)
    is_for_sale = models.BooleanField(default=True)
    is_condition_new = models.BooleanField(default=True)
    notes = models.TextField(null=True)
    owner = models.ForeignKey(Organization, null=True)

    def __str__(self):
        return '{}'.format(self.product_specification.name)


class RentalProduct(SerializedProduct):
    # qty_on_hand must equal 1
    # shelf_location
    # order_file
    # product_specification
    # serial_number
    # date_acquired
    # status
    # is_for_sale
    # is_condition_new
    # notes
    # owner
    times_rented = models.PositiveIntegerField(default=0)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return '{}'.format(self.product_specification.name)


class WardrobeItem(RentalProduct):
    # qty_on_hand must equal 1
    # shelf_location
    # order_file
    # product_specification
    # serial_number
    # date_acquired
    # status
    # is_for_sale
    # is_condition_new
    # notes
    # owner
    # times_rented
    # price_per_day
    size = models.TextField(max_length=40, blank=True)
    size_modifier = models.TextField(max_length=40, null=True, blank=True)
    gender = models.TextField(max_length=40, blank=True)
    color = models.TextField(max_length=40, blank=True)
    pattern = models.TextField(max_length=40, blank=True)
    start_year = models.PositiveIntegerField(null=True)
    end_year = models.PositiveIntegerField(null=True)

    def __str__(self):
        return '{}'.format(self.product_specification.name)


class RentalItem(TransactionLineItem):
    # amount
    # transaction
    pre_discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_out = models.DateTimeField(auto_now_add=True)
    date_in = models.DateTimeField(null=True)
    date_due = models.DateTimeField()
    discount_percent = models.PositiveSmallIntegerField(null=True)
    rental_product = models.ForeignKey(RentalProduct, related_name='+')

    def __str__(self):
        return '{}'.format(self.rental_product.product_specification.name)

    def calc_amount(self):
        rental_days_timedelta = self.date_due - self.date_out
        # an int multiplied by a Decimal results in a Decimal
        # self.rental_product.price_per_day is a float
        self.pre_discount_amount = Decimal(self.rental_product.price_per_day) * rental_days_timedelta.days
        # if isinstance(self.rental_product.price_per_day, float):
        #     print("self.rental_product.price_per_day is a Decimal.")
        # else:
        #     print("self.rental_product.price_per_day is NOT a Decimal.")

        # if isinstance(self.discount_percent, int):
        #     print("self.discount_percent is an int.")
        # else:
        #     print("self.discount_percent is NOT an int.")

        # self.discount_percent is an int
        if self.discount_percent is not None:
            discount_float = 1 - (self.discount_percent / 100)
            self.amount = self.pre_discount_amount * Decimal(discount_float)
        else:
            self.amount = self.pre_discount_amount


class Fee(TransactionLineItem):
    is_waived = models.BooleanField(default=False)
    rental_item = models.ForeignKey(RentalItem, related_name='+')

    class Meta:
        abstract = True


class LateFee(Fee):
    # amount
    # transaction
    # is_waived
    # rental_item
    days_late = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{} {}'.format(self.amount, self.days_late)

    def calc_amount(self):
        today = datetime.now()
        days_late_timedelta = today - self.rental_item.date_due
        self.days_late = days_late_timedelta.days
        self.amount = self.days_late * (
            Decimal(LATE_FEE_MULTIPLIER) * Decimal(self.rental_item.rental_product.price_per_day))


class DamageFee(Fee):
    # amount
    # transaction
    # is_waived
    # rental_item
    description = models.TextField(blank=True)

    def __str__(self):
        return '{} {}'.format(self.amount, self.description)


class SaleItem(TransactionLineItem):
    # amount
    # transaction
    quantity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(Product, related_name='+')

    def __str__(self):
        return '{}'.format(self.product.product_specification.name)

    def calc_amount(self):
        self.amount = self.product.product_specification.price * self.quantity





