from django.http import Http404, HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
import requests
from django.db.models import Q

templater = get_renderer('catalog')

#########################################################################
### View products

@view_function
def process_request(request):
    params = {}

    params["products"] = hmod.Product.objects.filter(
        SerializedProduct___is_for_sale=True) | hmod.Product.objects.instance_of(hmod.Product).not_instance_of(
        hmod.RentalProduct)

    return templater.render_to_response(request, '/catalog/templates/product.html', params)


@view_function
def detail(request):
    params = {}

    product_id = request.urlparams[0]

    try:
        product = hmod.Product.objects.get(id=product_id)
    except hmod.Product.DoesNotExist:
        return HttpResponseRedirect('/catalog/product/')

    params["product"] = product

    return templater.render_to_response(request, '/catalog/templates/product_detail.html', params)


@view_function
def search(request):
    params = {}

    # get the products filtered according to user's search criteria

    # params["products"] = products

    return templater.render_to_response(request, '/catalog/templates/product.search.html', params)

