# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428051766.329292
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/catalog/templates/shopping_cart.html'
_template_uri = 'shopping_cart.html'
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
        shopping_cart = context.get('shopping_cart', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)

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
        shopping_cart = context.get('shopping_cart', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)

        def content():
            return render_content(context)

        __M_writer = context.writer()
        __M_writer('\n\n')
        if shopping_cart == {}:
            __M_writer('    <div>Your cart is empty</div>\n')
        else:
            __M_writer('    <table class="table table-hover">\n        ')

            grand_total_price = 0
            grand_total_qty = 0

            __M_writer(
                '\n        <tr>\n            <th>ID</th>\n            <th>Product</th>\n            <th>Description</th>\n            <th>Product Price</th>\n            <th>Quantity</th>\n            <th>Amount</th>\n            <th></th>\n        </tr>\n')
            for product in shopping_cart:
                __M_writer('            ')

                qty = shopping_cart[product]
                price = product.product_specification.price * qty
                grand_total_price += price
                grand_total_qty += shopping_cart[product]

                __M_writer('\n            <tr>\n                <td>')
                __M_writer(str(product.id))
                __M_writer('</td>\n                <td>\n                    ')
                __M_writer(str(product.product_specification.name))
                __M_writer(
                    '\n                    <div class="cart_item_container">\n                        <img src="')
                __M_writer(str(STATIC_URL))
                __M_writer('catalog/media/images/product_pictures/')
                __M_writer(str(product.product_specification.photo.image))
                __M_writer('"/>\n                    </div>\n                </td>\n                <td>')
                __M_writer(str(product.product_specification.description))
                __M_writer('</td>\n                <td>$')
                __M_writer(str(product.product_specification.price))
                __M_writer('</td>\n                <td>')
                __M_writer(str(qty))
                __M_writer('</td>\n                <td>$')
                __M_writer(str(price))
                __M_writer('</td>\n                <td>\n                    <button data-product_id="')
                __M_writer(str(product.id))
                __M_writer(
                    '" type="button" class="remove btn btn-warning">Remove</button>\n                </td>\n            </tr>\n')
            __M_writer(
                '        <tr class="total">\n            <td>Total</td>\n            <td></td>\n            <td></td>\n            <td></td>\n            <td>')
            __M_writer(str(grand_total_qty))
            __M_writer(' item(s)</td>\n            <td>$')
            __M_writer(str(grand_total_price))
            __M_writer(
                '</td>\n            <td></td>\n        </tr>\n    </table>\n    <div class="text-right">\n        <button type="button" id="shop" class="btn btn-primary">Continue Shopping</button>\n        <a href="/catalog/checkout.shipping" class="btn btn-primary">Checkout</a>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 12, "65": 22, "66": 23, "67": 23, "74": 28, "75": 30, "76": 30, "77": 32, "78": 32, "79": 34, "80": 34, "81": 34, "82": 34, "83": 37, "84": 37, "85": 38, "86": 38, "87": 39, "88": 39, "89": 40, "90": 40, "27": 0, "92": 42, "93": 46, "94": 51, "95": 51, "96": 52, "97": 52, "91": 42, "36": 1, "103": 97, "46": 3, "54": 3, "55": 5, "56": 6, "57": 7, "58": 8, "59": 9}, "source_encoding": "ascii", "filename": "/Users/Nate/chf_dmp/catalog/templates/shopping_cart.html", "uri": "shopping_cart.html"}
__M_END_METADATA
"""
