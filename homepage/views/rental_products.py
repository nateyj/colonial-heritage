from django.http import Http404, HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
import requests

templater = get_renderer('homepage')

#########################################################################
### View rental_products

@view_function
def process_request(request):
    params = {}

    params["products"] = hmod.RentalProduct.objects.all()

    return templater.render_to_response(request, '/homepage/templates/rental_products.html', params)


@view_function
def detail(request):
    params = {}

    rental_product_id = request.urlparams[0]

    try:
        rental_product = hmod.RentalProduct.objects.get(id=rental_product_id)
    except hmod.RentalProduct.DoesNotExist:
        return HttpResponseRedirect('/homepage/rental_products/')

    params["product"] = rental_product

    return templater.render_to_response(request, '/homepage/templates/rental_product_detail.html', params)


@view_function
def search(request):
    params = {}

    # get the products filtered according to user's search criteria (by category or input field)

    # params["products"] = products

    return templater.render_to_response(request, '/catalog/templates/product.search.html', params)

