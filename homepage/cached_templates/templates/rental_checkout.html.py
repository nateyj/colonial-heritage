# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428511252.270336
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/rental_checkout.html'
_template_uri = 'rental_checkout.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        transaction_subtotal = context.get('transaction_subtotal', UNDEFINED)
        date_due = context.get('date_due', UNDEFINED)
        rental_cart = context.get('rental_cart', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        discount = context.get('discount', UNDEFINED)
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        transaction_subtotal = context.get('transaction_subtotal', UNDEFINED)
        date_due = context.get('date_due', UNDEFINED)
        rental_cart = context.get('rental_cart', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        discount = context.get('discount', UNDEFINED)
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<h1>Rental Summary</h1>\n<table class="table table-striped">\n    <tr>\n        <th>Rental Product</th>\n        <th>Price Per Day</th>\n        <th>Days Rented Out</th>\n        <th>Amount</th>\n    </tr>\n')
        for product in rental_cart:
            __M_writer('    <tr>\n        <td>\n            ')
            __M_writer(str( product.product_specification.name ))
            __M_writer('\n            <div class="cart_item_container">\n                <img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('catalog/media/images/product_pictures/')
            __M_writer(str( product.product_specification.photo.image ))
            __M_writer('"/>\n            </div>\n        </td>\n        <td>$')
            __M_writer(str( product.price_per_day ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( request.session['rental_days'] ))
            __M_writer('</td>\n        <td>$')
            __M_writer(str( rental_cart[product] ))
            __M_writer('</td>\n    </tr>\n')
        __M_writer('    <tr class="total">\n        <td></td>\n        <td></td>\n        <td>\n            Due Date: ')
        __M_writer(str( date_due.strftime('%b %d, %Y') ))
        __M_writer('\n        </td>\n        <td>\n            Subtotal $')
        __M_writer(str( transaction_subtotal ))
        __M_writer('<br>\n            Discount ')
        __M_writer(str( discount ))
        __M_writer('%<br>\n            Total $')
        __M_writer(str( request.session['rental_transaction_total'] ))
        __M_writer('\n        </td>\n    </tr>\n</table>\n\n<form method="POST">\n    <div>\n        <h2>\n            Billing Information\n            <button id="populate" type="button" class="btn btn-default btn-sm">Populate</button>\n        </h2>\n    </div>\n    <table>\n        ')
        __M_writer(str( form ))
        __M_writer('\n    </table>\n    <br><br>\n    <button class="submit_btn btn btn-primary" type="submit">Place Order</button>\n    <a class="btn btn-primary" href="/homepage/rental_products/">Cancel</a>\n</form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "rental_checkout.html", "line_map": {"64": 3, "65": 12, "66": 13, "67": 15, "68": 15, "69": 17, "70": 17, "71": 17, "72": 17, "73": 20, "74": 20, "75": 21, "76": 21, "77": 22, "78": 22, "79": 25, "80": 29, "81": 29, "82": 32, "83": 32, "84": 33, "85": 33, "86": 34, "87": 34, "88": 47, "89": 47, "27": 0, "95": 89, "41": 1, "51": 3}, "filename": "/Users/Nate/chf_dmp/homepage/templates/rental_checkout.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
