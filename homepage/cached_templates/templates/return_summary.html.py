# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428540835.122898
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/return_summary.html'
_template_uri = 'return_summary.html'
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
        damage_fee_total = context.get('damage_fee_total', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        rental_items = context.get('rental_items', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        late_fee_total = context.get('late_fee_total', UNDEFINED)
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
        damage_fee_total = context.get('damage_fee_total', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        rental_items = context.get('rental_items', UNDEFINED)
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        late_fee_total = context.get('late_fee_total', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<h1>Rental Return Summary</h1>\n<table class="table table-striped">\n    <tr>\n        <th>Rental Product</th>\n        <th>Late Fee Amount</th>\n        <th>Damage Fee Amount</th>\n        <th>Damage Description</th>\n    </tr>\n')
        for rental_item in rental_items:
            __M_writer('    <tr>\n        <td>\n            ')
            __M_writer(str( rental_item ))
            __M_writer('\n            <div class="cart_item_container">\n                <img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('catalog/media/images/product_pictures/')
            __M_writer(str( rental_item.rental_product.product_specification.photo.image ))
            __M_writer('"/>\n            </div>\n        </td>\n')
            if rental_items[rental_item][0] != '':
                __M_writer('            <td>$')
                __M_writer(str( rental_items[rental_item][0] ))
                __M_writer('</td>\n')
            else:
                __M_writer('            <td>N/A</td>\n')
            if rental_items[rental_item][1] != '':
                __M_writer('            <td>$')
                __M_writer(str( rental_items[rental_item][1] ))
                __M_writer('</td>\n')
            else:
                __M_writer('            <td>N/A</td>\n')
            if rental_items[rental_item][2] != '':
                __M_writer('            <td>')
                __M_writer(str( rental_items[rental_item][2] ))
                __M_writer('</td>\n')
            else:
                __M_writer('            <td>N/A</td>\n')
            __M_writer('    </tr>\n')
        __M_writer('    <tr class="total">\n        <td>Total</td>\n        <td>$')
        __M_writer(str( late_fee_total ))
        __M_writer('</td>\n        <td>$')
        __M_writer(str( damage_fee_total ))
        __M_writer('</td>\n        <td>$')
        __M_writer(str( request.session['fee_total'] ))
        __M_writer('</td>\n    </tr>\n</table>\n\n\n<form method="POST">\n    <div>\n        <h2>Billing Information</h2>\n    </div>\n    <table>\n        ')
        __M_writer(str( form ))
        __M_writer('\n    </table>\n    <br><br>\n    <button class="submit_btn btn btn-primary" type="submit">Finalize Return</button>\n    <a class="btn btn-primary" href="/homepage/rental_return/">Cancel</a>\n</form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/Nate/chf_dmp/homepage/templates/return_summary.html", "uri": "return_summary.html", "line_map": {"64": 13, "65": 15, "66": 15, "67": 17, "68": 17, "69": 17, "70": 17, "71": 20, "72": 21, "73": 21, "74": 21, "75": 22, "76": 23, "77": 25, "78": 26, "79": 26, "80": 26, "81": 27, "82": 28, "83": 30, "84": 31, "85": 31, "86": 31, "87": 32, "88": 33, "89": 35, "90": 37, "27": 0, "92": 39, "93": 40, "94": 40, "95": 41, "96": 41, "97": 51, "98": 51, "91": 39, "40": 1, "104": 98, "50": 3, "62": 3, "63": 12}}
__M_END_METADATA
"""
