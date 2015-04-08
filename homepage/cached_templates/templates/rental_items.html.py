# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428424228.536275
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
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        customer = context.get('customer', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        rental_items = context.get('rental_items', UNDEFINED)
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        customer = context.get('customer', UNDEFINED)
        def content():
            return render_content(context)
        rental_items = context.get('rental_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if rental_items == {}:
            __M_writer('<h1>')
            __M_writer(str( customer.get_full_name() ))
            __M_writer(' currently has no rental items that are checked out.</h1>\n')
        else:
            __M_writer('<h1>Checked Out Rental Items for ')
            __M_writer(str( customer.get_full_name() ))
            __M_writer('</h1>\n')
            for transaction in rental_items:
                __M_writer('<h3>Transaction ID: ')
                __M_writer(str( transaction.id ))
                __M_writer('</h3>\n<table class="table table-striped">\n    <tr>\n        <th>Line Item ID</th>\n        <th>Product</th>\n        <th>Date Due</th>\n        <th>Damage</th>\n        <th>Check In</th>\n    </tr>\n')
                for item in rental_items[transaction]:
                    __M_writer('    <tr class="item_container">\n        <td class="rental_item_id">')
                    __M_writer(str( item.id ))
                    __M_writer('</td>\n        <td>\n            ')
                    __M_writer(str( item ))
                    __M_writer('\n            <div>\n                <img src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('catalog/media/images/product_pictures/')
                    __M_writer(str( item.rental_product.product_specification.photo.image ))
                    __M_writer('"/>\n            </div>\n        </td>\n        <td>')
                    __M_writer(str( item.date_due.strftime('%b %d, %Y') ))
                    __M_writer('</td>\n        <td>\n            Fee\n            <input type="number" class="damage_fee">\n            <br/>\n            Description\n            <textarea class="damage_desc"></textarea>\n        </td>\n        <td>\n            <button type="button" class="return btn btn-primary">Check In</button>\n        </td>\n    </tr>\n')
                __M_writer('</table>\n<div>\n    <a href="/homepage/rental_return.summary" id="proceed" class="btn btn-primary">Proceed to Check In</a>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 8, "65": 9, "66": 10, "67": 10, "68": 10, "69": 19, "70": 20, "71": 21, "72": 21, "73": 23, "74": 23, "75": 25, "76": 25, "77": 25, "78": 25, "79": 28, "80": 28, "81": 41, "87": 81, "27": 0, "37": 1, "47": 3, "56": 3, "57": 5, "58": 6, "59": 6, "60": 6, "61": 7, "62": 8, "63": 8}, "source_encoding": "ascii", "filename": "/Users/Nate/chf_dmp/homepage/templates/rental_items.html", "uri": "rental_items.html"}
__M_END_METADATA
"""
