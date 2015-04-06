# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428091174.904554
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/rental_cart.html'
_template_uri = 'rental_cart.html'
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
        rental_cart = context.get('rental_cart', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)

        def content():
            return render_content(context._locals(__M_locals))

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
        rental_cart = context.get('rental_cart', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)

        def content():
            return render_content(context)

        __M_writer = context.writer()
        __M_writer('\n\n')
        if rental_cart == []:
            __M_writer('    <div>Your cart is empty</div>\n')
        else:
            __M_writer('    <table class="table table-hover">\n        ')

            grand_total_qty = 0

            __M_writer(
                '\n        <tr>\n            <th>ID</th>\n            <th>Rental Product</th>\n            <th>Price Per Day</th>\n            <th></th>\n        </tr>\n')
            for product in rental_cart:
                __M_writer('            ')

                grand_total_qty += 1

                __M_writer('\n            <tr>\n                <td>')
                __M_writer(str(product.id))
                __M_writer('</td>\n                <td>\n                    ')
                __M_writer(str(product.product_specification.name))
                __M_writer(
                    '\n                    <div class="cart_item_container">\n                        <img src="')
                __M_writer(str(STATIC_URL))
                __M_writer('catalog/media/images/product_pictures/')
                __M_writer(str(product.product_specification.photo.image))
                __M_writer('"/>\n                    </div>\n                </td>\n                <td>$')
                __M_writer(str(product.price_per_day))
                __M_writer('</td>\n                <td>\n                    <button data-product_id="')
                __M_writer(str(product.id))
                __M_writer(
                    '" type="button" class="remove btn btn-warning">Remove</button>\n                </td>\n            </tr>\n')
            __M_writer(
                '        <tr class="total">\n            <td>Total</td>\n            <td></td>\n            <td>')
            __M_writer(str(grand_total_qty))
            __M_writer(
                ' item(s)</td>\n            <td></td>\n        </tr>\n    </table>\n    <p id="buttons">\n        <form method="POST" class="text-left" action="/homepage/rental_cart">\n            ')
            __M_writer(str(form))
            __M_writer(
                '\n            <div class="pull-right">\n                <button type="button" id="shop" class="btn btn-primary">Continue Shopping</button>\n                <button type="submit" id="checkout" class="btn btn-primary">Checkout</button>\n            </div>\n        </form>\n    </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "rental_cart.html", "line_map": {"65": 11, "66": 18, "67": 19, "68": 19, "72": 21, "73": 23, "74": 23, "75": 25, "76": 25, "77": 27, "78": 27, "79": 27, "80": 27, "81": 30, "82": 30, "83": 32, "84": 32, "85": 36, "86": 39, "87": 39, "88": 45, "89": 45, "27": 0, "95": 89, "37": 1, "47": 3, "56": 3, "57": 5, "58": 6, "59": 7, "60": 8, "61": 9}, "source_encoding": "ascii", "filename": "/Users/Nate/chf_dmp/homepage/templates/rental_cart.html"}
__M_END_METADATA
"""
