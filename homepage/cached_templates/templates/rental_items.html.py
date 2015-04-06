# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428203336.96966
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/rental_items.html'
_template_uri = 'rental_items.html'
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


def render_body(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        rental_items = context.get('rental_items', UNDEFINED)
        customer = context.get('customer', UNDEFINED)
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
        rental_items = context.get('rental_items', UNDEFINED)
        customer = context.get('customer', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)

        def content():
            return render_content(context)

        __M_writer = context.writer()
        __M_writer('\n\n<div class="text-left">\n    <h1>Checked Out Rental Items for ')
        __M_writer(str(customer.get_full_name()))
        __M_writer('</h1>\n</div>\n\n')
        if rental_items == []:
            __M_writer('    <h1>')
            __M_writer(str(customer.get_full_name()))
            __M_writer(', you currently have no rental items that are checked out.</h1>\n')
        else:
            __M_writer('    <h1>Checked Out Rental Items for ')
            __M_writer(str(customer.get_full_name()))
            __M_writer('</h1>\n')
            for transaction in rental_items:
                __M_writer('        <h3>Transaction ID: ')
                __M_writer(str(transaction.id))
                __M_writer(
                    '</h3>\n        <table class="table table-striped">\n            <tr>\n                <th>Line Item ID</th>\n                <th>Product</th>\n                <th>Date Due</th>\n                <th>Damage</th>\n                <th>Check In</th>\n            </tr>\n')
                for item in rental_items[transaction]:
                    __M_writer(
                        '                <tr class="item_container">\n                    <td class="rental_item_id">')
                    __M_writer(str(item.id))
                    __M_writer('</td>\n                    <td>\n                        ')
                    __M_writer(str(item))
                    __M_writer('\n                        <div>\n                            <img src="')
                    __M_writer(str(STATIC_URL))
                    __M_writer('catalog/media/images/product_pictures/')
                    __M_writer(str(item.rental_product.product_specification.photo.image))
                    __M_writer(
                        '"/>\n                        </div>\n                    </td>\n                    <td>')
                    __M_writer(str(item.date_due.strftime('%b %d, %Y')))
                    __M_writer(
                        '</td>\n                    <td>\n                        Fee\n                        <input type="number" class="damage_fee">\n                        <br/>\n                        Description\n                        <textarea class="damage_desc"></textarea>\n                    </td>\n                    <td>\n                        <button type="button" class="return btn btn-primary">Check In</button>\n                    </td>\n                </tr>\n')
                __M_writer(
                    '        </table>\n        <div>\n            <a href="/homepage/rental_return.summary" id="proceed" class="btn btn-primary">Proceed to Check In</a>\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/Nate/chf_dmp/homepage/templates/rental_items.html", "uri": "rental_items.html", "line_map": {"64": 12, "65": 12, "66": 12, "67": 13, "68": 14, "69": 14, "70": 14, "71": 23, "72": 24, "73": 25, "74": 25, "75": 27, "76": 27, "77": 29, "78": 29, "79": 29, "80": 29, "81": 32, "82": 32, "83": 45, "89": 83, "27": 0, "37": 1, "47": 3, "56": 3, "57": 6, "58": 6, "59": 9, "60": 10, "61": 10, "62": 10, "63": 11}}
__M_END_METADATA
"""
