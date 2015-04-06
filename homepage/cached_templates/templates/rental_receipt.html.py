# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428099811.41368
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/rental_receipt.html'
_template_uri = 'rental_receipt.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base_ajax.htm', _template_uri)


def render_body(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        transaction = context.get('transaction', UNDEFINED)
        rental_cart = context.get('rental_cart', UNDEFINED)

        def content():
            return render_content(context._locals(__M_locals))

        rental_charge_resp = context.get('rental_charge_resp', UNDEFINED)
        request = context.get('request', UNDEFINED)
        user = context.get('user', UNDEFINED)
        date_due = context.get('date_due', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        transaction = context.get('transaction', UNDEFINED)
        rental_cart = context.get('rental_cart', UNDEFINED)

        def content():
            return render_content(context)

        rental_charge_resp = context.get('rental_charge_resp', UNDEFINED)
        request = context.get('request', UNDEFINED)
        user = context.get('user', UNDEFINED)
        date_due = context.get('date_due', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <p style="font-weight: bold;">Hello ')
        __M_writer(str(user.get_full_name()))
        __M_writer(
            ",</p>\n    <p>Thank you for renting from us! We'll send a notification email the day before your items are due.</p>\n    <p>Your items are due on <b>")
        __M_writer(str(date_due.strftime('%b %d, %Y')))
        __M_writer(
            '</b></p>\n    <table class="table table-striped">\n        <tr>\n            <th>Rental Product</th>\n            <th>Price Per Day</th>\n            <th>Days Rented Out</th>\n            <th>Amount</th>\n        </tr>\n')
        for rental_item in rental_cart:
            __M_writer('            <tr>\n                <td>')
            __M_writer(str(rental_item.rental_product.product_specification.name))
            __M_writer('</td>\n                <td>$')
            __M_writer(str(rental_item.rental_product.price_per_day))
            __M_writer('</td>\n                <td>')
            __M_writer(str(request.session['rental_days']))
            __M_writer('</td>\n                <td>$')
            __M_writer(str(rental_item.amount))
            __M_writer('</td>\n            </tr>\n')
        __M_writer(
            '        <tr>\n            <td></td>\n            <td></td>\n            <td></td>\n            <td></td>\n        </tr>\n        <tr style="font-weight: bold;">\n            <td>')
        __M_writer(str(transaction.get_rental_item_count()))
        __M_writer(' item(s)</td>\n            <td></td>\n            <td>Subtotal</td>\n            <td>$')
        __M_writer(str(transaction.pre_discount_total))
        __M_writer(
            '</td>\n        </tr>\n        <tr>\n            <td></td>\n            <td></td>\n            <td>Discount</td>\n            <td>')
        __M_writer(str(request.session['discount']))
        __M_writer(
            '%</td>\n        </tr>\n        <tr style="font-weight: bold;">\n            <td></td>\n            <td></td>\n            <td>Total</td>\n            <td>$')
        __M_writer(str(transaction.total))
        __M_writer(
            '</td>\n        </tr>\n        <tr style="font-weight: bold;">\n            <td></td>\n            <td></td>\n            <td>Payment</td>\n')
        if request.session['discount'] != 100:
            __M_writer('                <td>$')
            __M_writer(str(rental_charge_resp['Amount']))
            __M_writer(' ')
            __M_writer(str(rental_charge_resp['Currency']))
            __M_writer('</td>\n')
        else:
            __M_writer('                <td>$0.00 usd</td>\n')
        __M_writer('        </tr>\n    </table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 4, "65": 6, "66": 6, "67": 14, "68": 15, "69": 16, "70": 16, "71": 17, "72": 17, "73": 18, "74": 18, "75": 19, "76": 19, "77": 22, "78": 29, "79": 29, "80": 32, "81": 32, "82": 38, "83": 38, "84": 44, "85": 44, "86": 50, "87": 51, "88": 51, "89": 51, "90": 51, "27": 0, "92": 52, "93": 53, "94": 55, "91": 51, "100": 94, "40": 1, "50": 3, "62": 3, "63": 4}, "uri": "rental_receipt.html", "filename": "/Users/Nate/chf_dmp/homepage/templates/rental_receipt.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
