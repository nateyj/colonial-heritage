# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 11:15
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('security_question', models.TextField(blank=True, max_length=200, null=True)),
                ('security_answer', models.TextField(blank=True, max_length=200, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.TextField(blank=True, max_length=200)),
                ('address2', models.TextField(blank=True, max_length=200, null=True)),
                ('city', models.TextField(blank=True, max_length=100)),
                ('state', models.TextField(blank=True, max_length=2)),
                ('zip_code', models.TextField(blank=True, max_length=20)),
                ('country', models.TextField(blank=True, default='United States', max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_addresses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['country', 'state', 'city', 'zip_code', 'address1', 'address2'],
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('place_number', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ArtisanItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artisan_items', to='homepage.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='DamageFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_waived', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('map_file_name', models.FileField(null=True, upload_to='files/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='LateFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_waived', models.BooleanField(default=False)),
                ('days_late', models.PositiveSmallIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_name', models.TextField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParticipantRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=200)),
                ('type', models.TextField(blank=True, max_length=40)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField(blank=True, max_length=40)),
                ('extension', models.PositiveSmallIntegerField(null=True)),
                ('type', models.TextField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Photograph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_taken', models.DateTimeField(null=True)),
                ('place_taken', models.TextField(blank=True, max_length=200, null=True)),
                ('name', models.TextField(blank=True, max_length=1000)),
                ('image', models.ImageField(upload_to='images')),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_photos', to='homepage.Area')),
                ('artisan_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artisan_item_photos', to='homepage.ArtisanItem')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_photos', to='homepage.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty_on_hand', models.PositiveIntegerField(default=1)),
                ('shelf_location', models.TextField(blank=True, max_length=40, null=True)),
                ('order_file', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('order_form_name', models.TextField(max_length=200, null=True)),
                ('production_time', models.TextField(max_length=200, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='homepage.Category')),
                ('photo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Photograph')),
            ],
        ),
        migrations.CreateModel(
            name='PublicEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RentalItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('pre_discount_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('date_out', models.DateTimeField(auto_now_add=True)),
                ('date_in', models.DateTimeField(null=True)),
                ('date_due', models.DateTimeField()),
                ('discount_percent', models.PositiveSmallIntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('pre_discount_total', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('credit_card_charge_ID', models.TextField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL)),
                ('ships_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=200)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homepage.Address')),
                ('event', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Event')),
                ('venue_contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='homepage.Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('organization_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='homepage.Organization')),
                ('last_name', models.TextField(blank=True, max_length=50)),
                ('birth_date', models.DateField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('homepage.organization',),
        ),
        migrations.CreateModel(
            name='SerializedProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='homepage.Product')),
                ('serial_number', models.TextField(max_length=12, null=True, unique=True)),
                ('date_acquired', models.DateField(auto_now_add=True)),
                ('status', models.TextField(blank=True, max_length=40, null=True)),
                ('is_for_sale', models.BooleanField(default=True)),
                ('is_condition_new', models.BooleanField(default=True)),
                ('notes', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('homepage.product',),
        ),
        migrations.AddField(
            model_name='saleitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='homepage.Product'),
        ),
        migrations.AddField(
            model_name='saleitem',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Transaction'),
        ),
        migrations.AddField(
            model_name='rentalitem',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Transaction'),
        ),
        migrations.AddField(
            model_name='productspecification',
            name='producer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Organization'),
        ),
        migrations.AddField(
            model_name='product',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_homepage.product_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_specification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='homepage.ProductSpecification'),
        ),
        migrations.AddField(
            model_name='photograph',
            name='public_event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='public_event_photos', to='homepage.PublicEvent'),
        ),
        migrations.AddField(
            model_name='photograph',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='venue_photos', to='homepage.Venue'),
        ),
        migrations.AddField(
            model_name='phone',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_phones', to='homepage.Organization'),
        ),
        migrations.AddField(
            model_name='phone',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_phones', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organization',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Address'),
        ),
        migrations.AddField(
            model_name='organization',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_homepage.organization_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='latefee',
            name='rental_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='homepage.RentalItem'),
        ),
        migrations.AddField(
            model_name='latefee',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Transaction'),
        ),
        migrations.AddField(
            model_name='event',
            name='public_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='homepage.PublicEvent'),
        ),
        migrations.AddField(
            model_name='damagefee',
            name='rental_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='homepage.RentalItem'),
        ),
        migrations.AddField(
            model_name='damagefee',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Transaction'),
        ),
        migrations.AddField(
            model_name='area',
            name='public_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areas', to='homepage.PublicEvent'),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='homepage.Person')),
                ('date_hired', models.DateField()),
                ('wage', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'abstract': False,
            },
            bases=('homepage.person',),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='homepage.Person')),
                ('bio_sketch', models.TextField(blank=True, max_length=1000)),
                ('emergency_contact_name', models.TextField(blank=True, max_length=200)),
                ('emergency_contact_relationship', models.TextField(blank=True, max_length=200)),
                ('emergency_contact_phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Phone')),
            ],
            options={
                'abstract': False,
            },
            bases=('homepage.person',),
        ),
        migrations.CreateModel(
            name='RentalProduct',
            fields=[
                ('serializedproduct_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='homepage.SerializedProduct')),
                ('times_rented', models.PositiveIntegerField(default=0)),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('homepage.serializedproduct',),
        ),
        migrations.AddField(
            model_name='serializedproduct',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Organization'),
        ),
        migrations.AddField(
            model_name='person',
            name='account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='WardrobeItem',
            fields=[
                ('rentalproduct_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='homepage.RentalProduct')),
                ('size', models.TextField(blank=True, max_length=40)),
                ('size_modifier', models.TextField(blank=True, max_length=40, null=True)),
                ('gender', models.TextField(blank=True, max_length=40)),
                ('color', models.TextField(blank=True, max_length=40)),
                ('pattern', models.TextField(blank=True, max_length=40)),
                ('start_year', models.PositiveIntegerField(null=True)),
                ('end_year', models.PositiveIntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('homepage.rentalproduct',),
        ),
        migrations.AddField(
            model_name='transaction',
            name='checked_in_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checked_in_set', to='homepage.Employee'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='checked_out_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checked_out_set', to='homepage.Employee'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='handled_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='handledby_set', to='homepage.Employee'),
        ),
        migrations.AddField(
            model_name='rentalitem',
            name='rental_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='homepage.RentalProduct'),
        ),
        migrations.AddField(
            model_name='photograph',
            name='participant',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo_id', to='homepage.Participant'),
        ),
        migrations.AddField(
            model_name='participantrole',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Participant'),
        ),
        migrations.AddField(
            model_name='area',
            name='coordinator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coordinates', to='homepage.Participant'),
        ),
        migrations.AddField(
            model_name='area',
            name='participants',
            field=models.ManyToManyField(through='homepage.ParticipantRole', to='homepage.Participant'),
        ),
        migrations.AddField(
            model_name='area',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supervises', to='homepage.Employee'),
        ),
    ]