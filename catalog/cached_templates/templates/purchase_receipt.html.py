# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428028770.366532
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/catalog/templates/purchase_receipt.html'
_template_uri = 'purchase_receipt.html'
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
    return runtime._inherit_from(context, '/catalog/templates/base_ajax.htm', _template_uri)


def render_body(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        charge_resp = context.get('charge_resp', UNDEFINED)

        def content():
            return render_content(context._locals(__M_locals))

        shopping_cart = context.get('shopping_cart', UNDEFINED)
        user = context.get('user', UNDEFINED)
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
        charge_resp = context.get('charge_resp', UNDEFINED)

        def content():
            return render_content(context)

        shopping_cart = context.get('shopping_cart', UNDEFINED)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <p style="font-weight: bold;">Hello, ')
        __M_writer(str(user.get_full_name()))
        __M_writer(
            '</p>\n    <p>Thank you for shopping with us! We\'ll send a confirmation when your order ships.</p>\n    <table class="table table-hover">\n        ')

        grand_total_amount = 0
        grand_total_qty = 0

        __M_writer(
            '\n        <tr>\n            <th>Product</th>\n            <th>Product Price</th>\n            <th>Quantity</th>\n            <th>Amount</th>\n        </tr>\n')
        for product in shopping_cart:
            __M_writer('            ')

            qty = shopping_cart[product]
            amount = product.product_specification.price * qty
            grand_total_amount += amount
            grand_total_qty += shopping_cart[product]

            __M_writer('\n            <tr>\n                <td>')
            __M_writer(str(product.product_specification.name))
            __M_writer('</td>\n                <td>$')
            __M_writer(str(product.product_specification.price))
            __M_writer('</td>\n                <td>')
            __M_writer(str(qty))
            __M_writer('</td>\n                <td>$')
            __M_writer(str(amount))
            __M_writer('</td>\n            </tr>\n')
        __M_writer(
            '        <tr style="font-weight: bold;">\n            <td>Total</td>\n            <td></td>\n            <td>')
        __M_writer(str(grand_total_qty))
        __M_writer(' item(s)</td>\n            <td>$')
        __M_writer(str(grand_total_amount))
        __M_writer(
            '</td>\n        </tr>\n        <tr style="font-weight: bold;">\n            <td></td>\n            <td></td>\n            <td>Payment</td>\n            <td>$')
        __M_writer(str(charge_resp['Amount']))
        __M_writer(' ')
        __M_writer(str(charge_resp['Currency']))
        __M_writer('</td>\n        </tr>\n    </table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 10, "65": 17, "66": 18, "67": 18, "74": 23, "75": 25, "76": 25, "77": 26, "78": 26, "79": 27, "80": 27, "81": 28, "82": 28, "83": 31, "84": 34, "85": 34, "86": 35, "87": 35, "88": 41, "89": 41, "90": 41, "27": 0, "97": 91, "91": 41, "37": 1, "47": 3, "56": 3, "57": 4, "58": 4, "59": 7}, "filename": "/Users/Nate/chf_dmp/catalog/templates/purchase_receipt.html", "source_encoding": "ascii", "uri": "purchase_receipt.html"}
__M_END_METADATA
"""
