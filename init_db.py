__author__ = 'Nate'

# !/usr/bin/env python

# initialize django
import os, sys, django, subprocess

os.environ['DJANGO_SETTINGS_MODULE'] = 'chf_dmp.settings'
django.setup()

# normal import
import homepage.models as hmod
from datetime import datetime, timedelta
from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection

##### DROP DATABASE, RECREATE IT, THEN MIGRATE IT #################

cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])

###################################################################
##### Delete all permissions and groups
Permission.objects.all().delete()
Group.objects.all().delete()

# create all the tables (python manage.py migrate)

# creating data for users and groups
u_nate = hmod.SiteUser()
u_nate.first_name = 'Nathan'
u_nate.last_name = 'Johnson'
u_nate.username = 'nathan'
u_nate.set_password('Password1')
u_nate.email = 'nate8etan@gmail.com'
u_nate.is_superuser = True
u_nate.save()

gAdmin = hmod.Group()
gAdmin.name = 'Administrator'
gAdmin.save()
gAdmin.user_set.add(u_nate)

u = hmod.SiteUser()
u.first_name = 'Kyle'
u.last_name = 'Tucker'
u.username = 'kyle'
u.set_password('Password1')
u.is_superuser = False
u.save()

gMan = hmod.Group()
gMan.name = 'Manager'
gMan.save()
gMan.user_set.add(u)

u_weston = hmod.SiteUser()
u_weston.first_name = 'Weston'
u_weston.last_name = 'Rhodes'
u_weston.username = 'weston'
u_weston.set_password('Password1')
u_weston.is_superuser = False
u_weston.save()

gAgent = hmod.Group()
gAgent.name = 'Agent'
gAgent.save()
gAgent.user_set.add(u_weston)

u_erick = hmod.SiteUser()
u_erick.first_name = 'Erick'
u_erick.last_name = 'Pence'
u_erick.username = 'erick'
u_erick.set_password('Password1')
u_erick.email = 'erickpence09@gmail.com'
u_erick.is_superuser = False
u_erick.save()

u_scooby = hmod.SiteUser()
u_scooby.first_name = 'Scooby'
u_scooby.last_name = 'Doo'
u_scooby.username = 'scoobysnacks'
u_scooby.set_password('ruhroh')
u_scooby.is_superuser = False
u_scooby.save()

gGuest = hmod.Group()
gGuest.name = 'Guest'
gGuest.save()
gGuest.user_set.add(u_erick)
gGuest.user_set.add(u_scooby)

# creating addresses
address1 = hmod.Address()
address1.address1 = '777 Heavenly Way'
address1.city = 'Zion'
address1.state = 'MO'
address1.zip_code = '99999'
address1.user = u
address1.save()

address2 = hmod.Address()
address2.address1 = '123 Count Ct'
address2.city = 'Fingers'
address2.state = 'FL'
address2.zip_code = '11111'
address2.save()

# creating data for organizations
o_disney = hmod.Organization()
o_disney.given_name = 'Disney'
o_disney.email = 'mickeymouse@gmail.com'
o_disney.address = address1
o_disney.save()

o_toysrus = hmod.Organization()
o_toysrus.given_name = '''Toys "R" Us'''
o_toysrus.email = 'toys@gmail.com'
o_toysrus.address = address2
o_toysrus.save()

# creating employees
e = hmod.Employee()
e.given_name = u_nate.first_name
e.email = u_nate.email
e.address = address1
e.last_name = u_nate.last_name
e.birth_date = '1990-08-20'
e.account = u_nate
e.date_hired = '2015-04-01'
e.wage = 20
e.save()

e = hmod.Employee()
e.given_name = u_weston.first_name
e.address = address2
e.last_name = u_weston.last_name
e.birth_date = '1992-08-14'
e.account = u_weston
e.date_hired = '2015-04-01'
e.wage = 25
e.save()


# creating data for Phone
phone1 = hmod.Phone()
phone1.number = '208-999-999'
phone1.type = 'mobile'
phone1.user = u
phone1.save()

phone2 = hmod.Phone()
phone2.number = '801-999-999'
phone2.type = 'office'
phone2.organization = o_toysrus
phone2.user = u
phone2.save()

# particpants
p = hmod.Participant()
p.given_name = u_erick.first_name
p.email = u_erick.email
p.address = address2
p.last_name = u_erick.last_name
p.birth_date = '1990-8-7'
p.account = u_erick
p.bio_sketch = ''
p.emergency_contact_name = 'Nathan Johnson'
p.emergency_contact_phone = phone2
p.emergency_contact_relationship = 'friend'
p.save()

# creating categories
c_apparel = hmod.Category()
c_apparel.name = 'Apparel'
c_apparel.save()

c_toy = hmod.Category()
c_toy.name = 'Toy'
c_toy.save()

c_access = hmod.Category()
c_access.name = 'Accessories'
c_access.save()

# creating photographs
photo_hat = hmod.Photograph()
photo_hat.name = 'Colonial Hat'
photo_hat.image = 'colonial_hat_men.jpg'
photo_hat.save()

photo_pistol = hmod.Photograph()
photo_pistol.name = 'Toy Pistol'
photo_pistol.image = 'pistol.jpeg'
photo_pistol.save()

photo_breeches = hmod.Photograph()
photo_breeches.name = 'Red Breeches'
photo_breeches.image = 'breeches.jpg'
photo_breeches.save()

photo_coat = hmod.Photograph()
photo_coat.name = 'Frock Coat'
photo_coat.image = 'colonial_coat.jpg'
photo_coat.save()

photo_boots = hmod.Photograph()
photo_boots.name = 'Boots'
photo_boots.image = 'boots.jpg'
photo_boots.save()

photo_watch = hmod.Photograph()
photo_watch.name = 'Pocket Watch'
photo_watch.image = 'pocket_watch.jpg'
photo_watch.save()


# creating product specifications
ps_hat = hmod.ProductSpecification()
ps_hat.name = 'Hat'
ps_hat.price = 12.99
ps_hat.description = 'Colonial Hat - Men'
ps_hat.category = c_apparel
ps_hat.photo = photo_hat
ps_hat.save()

ps_pistol = hmod.ProductSpecification()
ps_pistol.name = 'Pistol'
ps_pistol.price = 7.99
ps_pistol.description = 'Colonial Pistol: Ages 5+'
ps_pistol.category = c_toy
ps_pistol.photo = photo_pistol
ps_pistol.save()

ps_breeches = hmod.ProductSpecification()
ps_breeches.name = 'Breeches'
ps_breeches.price = 19.99
ps_breeches.description = 'Learn how to pronounce this from Gove Allen.'
ps_breeches.category = c_apparel
ps_breeches.photo = photo_breeches
ps_breeches.save()

ps_coat = hmod.ProductSpecification()
ps_coat.name = photo_coat.name
ps_coat.price = 39.99
ps_coat.description = '''White tabby weave wool, fulled, napped and shorn (broadcloth), embroidered with silver threads, bullion, and sequins; lined with twill worsted "shalloon" and cotton/linen napped twill "fustian."'''
ps_coat.category = c_apparel
ps_coat.photo = photo_coat
ps_coat.save()

ps_boots = hmod.ProductSpecification()
ps_boots.name = 'Two Left Boots'
ps_boots.price = 34.57
ps_boots.description = "Weathered, leather, knee-high colonial style boots."
ps_boots.category = c_apparel
ps_boots.photo = photo_boots
ps_boots.save()

ps_watch = hmod.ProductSpecification()
ps_watch.name = 'Pocket Watch'
ps_watch.price = 23.89
ps_watch.description = "Old fashioned pocket watch made of copper, brass, nickel, and gold. Worn by Thomas Edison himself."
ps_watch.category = c_access
ps_watch.photo = photo_watch
ps_watch.save()

# creating products
product_hat = hmod.Product()
product_hat.qty_on_hand = 50
product_hat.product_specification = ps_hat
product_hat.save()

product_pistol = hmod.Product()
product_pistol.qty_on_hand = 100
product_pistol.product_specification = ps_pistol
product_pistol.save()

# creating rental products
rp_watch = hmod.RentalProduct()
rp_watch.qty_on_hand = 1
rp_watch.product_specification = ps_watch
rp_watch.is_condition_new = False
rp_watch.times_rented = 1
rp_watch.price_per_day = 0.75
rp_watch.save()

# creating wardrobe items
wardrobe_item1 = hmod.WardrobeItem()
wardrobe_item1.qty_on_hand = 1
wardrobe_item1.product_specification = ps_breeches
wardrobe_item1.is_for_sale = False
wardrobe_item1.is_condition_new = False
wardrobe_item1.times_rented = 1
wardrobe_item1.price_per_day = 1.99
wardrobe_item1.size = 'L'
wardrobe_item1.gender = 'M'
wardrobe_item1.color = 'red'
wardrobe_item1.pattern = 'solid'
wardrobe_item1.save()

wi_coat = hmod.WardrobeItem()
wi_coat.qty_on_hand = 1
wi_coat.product_specification = ps_coat
wi_coat.is_for_sale = False
wi_coat.is_condition_new = False
wi_coat.price_per_day = 2.99
wi_coat.size = 'L'
wi_coat.gender = 'M'
wi_coat.color = 'white'
wi_coat.pattern = 'solid'
wi_coat.save()

wi_boots = hmod.WardrobeItem()
wi_boots.qty_on_hand = 1
wi_boots.product_specification = ps_boots
wi_boots.is_for_sale = False
wi_boots.is_condition_new = False
wi_boots.price_per_day = 3.50
wi_boots.size = '12'
wi_boots.gender = 'M'
wi_boots.color = 'brown'
wi_boots.pattern = 'solid'
wi_boots.save()



# rental items
today = datetime.now()
date_out = today - timedelta(days=100)
# '2014-12-31' dates must be in this format or computer won't be happy

# rental transactions
t1 = hmod.Transaction()
t1.customer = u
t1.checked_out_by = e
t1.save()

# I have to set the date after the object is saved, because auto-stamping is on for the transaction.date attribute, so
# upon the instantiation of a transaction, the date is pre-generated and won't allow an override until it is saved
t1.date = date_out
t1.save()

t2 = hmod.Transaction()
t2.customer = u_nate
t2.checked_out_by = e
t2.save()

t2.date = date_out
t2.save()

t3 = hmod.Transaction()
t3.customer = u_weston
t3.checked_out_by = e
t3.save()

t3.date = date_out
t3.save()

t4 = hmod.Transaction()
t4.customer = u_erick
t4.checked_out_by = e
t4.save()

t4.date = date_out
t4.save()

trans_list = [t1, t2, t3, t4]

# next rental item associated with one transaction
date_due79 = date_out + timedelta(days=21)

ri1 = hmod.RentalItem()
ri1.discount_percent = 0
ri1.transaction = t1
ri1.date_due = date_due79
ri1.rental_product = wardrobe_item1
ri1.save()

ri1.date_out = date_out
ri1.calc_amount()  # can't call this until we have the correct date out
ri1.save()

# next two rental items associated with one transaction
date_due45 = date_out + timedelta(days=55)

ri2 = hmod.RentalItem()
ri2.discount_percent = 0
ri2.transaction = t2
ri2.date_due = date_due45
ri2.rental_product = wi_coat
ri2.save()

ri2.date_out = date_out
ri2.calc_amount()
ri2.save()

ri3 = hmod.RentalItem()
ri3.discount_percent = 0
ri3.transaction = t2
ri3.date_due = date_due45
ri3.rental_product = wardrobe_item1
ri3.save()

ri3.date_out = date_out
ri3.calc_amount()
ri3.save()

# next three rental items associated with one transaction
date_due91 = date_out + timedelta(days=9)

ri4 = hmod.RentalItem()
ri4.discount_percent = 0
ri4.transaction = t3
ri4.date_due = date_due91
ri4.rental_product = wi_boots
ri4.save()

ri4.date_out = date_out
ri4.calc_amount()
ri4.save()

ri5 = hmod.RentalItem()
ri5.discount_percent = 0
ri5.transaction = t3
ri5.date_due = date_due91
ri5.rental_product = rp_watch
ri5.save()

ri5.date_out = date_out
ri5.calc_amount()
ri5.save()

ri6 = hmod.RentalItem()
ri6.discount_percent = 0
ri6.transaction = t3
ri6.date_due = date_due91
ri6.rental_product = wi_coat
ri6.save()

ri6.date_out = date_out
ri6.calc_amount()
ri6.save()

# next four rental items associated with one transaction
date_due10 = date_out + timedelta(days=90)

ri7 = hmod.RentalItem()
ri7.discount_percent = 0
ri7.transaction = t4
ri7.date_due = date_due10
ri7.rental_product = wi_boots
ri7.save()

ri7.date_out = date_out
ri7.calc_amount()
ri7.save()

ri8 = hmod.RentalItem()
ri8.discount_percent = 0
ri8.transaction = t4
ri8.date_due = date_due10
ri8.rental_product = rp_watch
ri8.save()

ri8.date_out = date_out
ri8.calc_amount()
ri8.save()

for t in trans_list:
    t.calc_rental_total()
    t.save()

# l = hmod.LateFee()
# l.transaction = t4
# l.rental_item = ri8
# l.calc_amount()
# l.save()

# public events
public_event = hmod.PublicEvent()
public_event.name = 'Colonial Heritage Festival'
public_event.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
public_event.save()

# events (instances of a public event)
event = hmod.Event()
event.start_date = '2015-7-1'
event.end_date = '2015-7-12'
event.public_event = public_event
event.save()

# areas
a_bakery = hmod.Area()
a_bakery.name = 'Bakery'
a_bakery.description = 'See how bread was made back in the olden days. Smells good. Tastes better.'
a_bakery.place_number = 1
a_bakery.coordinator = p
a_bakery.supervisor = e
a_bakery.public_event = public_event
a_bakery.save()

a_coop = hmod.Area()
a_coop.name = 'Cooperage'
a_coop.description = "Craftsman who make buckets, barrels and casks from wood bound together with metal hoops are called a coopers and they work here. During the American colonial period, barrels and casks played a major role in transporting goods of many varieties between England and the colonies. They were very durable and easily moved even when very heavily loaded. Oak barrels were vital to the creation and storage of the products of distillers like George Washington and brewers like Samuel Adams."
a_coop.place_number = 2
a_coop.coordinator = p
a_coop.supervisor = e
a_coop.public_event = public_event
a_coop.save()

# artisan items
ai_bread = hmod.ArtisanItem()
ai_bread.name = 'Fresh Baked Bread'
ai_bread.description = "Made old school, it's the freshest bread you'll find of its kind."
ai_bread.price = 2.50
ai_bread.area = a_bakery
ai_bread.save()

ai_chef = hmod.ArtisanItem()
ai_chef.name = 'Colonial Chef Hat'
ai_chef.description = "It looks new school, but they really did where these back then."
ai_chef.price = 9.99
ai_chef.area = a_bakery
ai_chef.save()

ai_basket = hmod.ArtisanItem()
ai_basket.name = 'Handwoven Basket'
ai_basket.description = "This handwoven basket has handles for you to carry your festival items in."
ai_basket.price = 12.99
ai_basket.area = a_coop
ai_basket.save()

ai_mug = hmod.ArtisanItem()
ai_mug.name = 'Old Fashioned Barrel Mug'
ai_mug.description = "Although it's made of wood, it's tight like unto a dish. Feel like your back in time when you drink with your friends."
ai_mug.price = 10.99
ai_mug.area = a_coop
ai_mug.save()

# artisan item photos
for data in [
    ['Bread', 'bread.jpg', ai_bread],
    ['Chef Hat', 'chef_hat.jpg', ai_chef],
    ['Basket', 'basket.jpg', ai_basket],
    ['Barrel Mug', 'barrel_mug.jpg', ai_mug],
]:
    photo = hmod.Photograph()
    photo.name = data[0]
    photo.image = data[1]
    photo.artisan_item = data[2]
    photo.save()

# area photos
for data in [
    ['Cooperage', 'cooperage.jpg', a_coop],
    ['Bakery', 'bakery.jpg', a_bakery],
]:
    photo = hmod.Photograph()
    photo.name = data[0]
    photo.image = data[1]
    photo.area = data[2]
    photo.save()

# public event photos
for data in [
    ['Line of Fire', 'festival.jpg', public_event],
]:
    photo = hmod.Photograph()
    photo.name = data[0]
    photo.image = data[1]
    photo.public_event = data[2]
    photo.save()


