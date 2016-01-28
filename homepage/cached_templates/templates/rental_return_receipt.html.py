# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428628661.885825
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/rental_return_receipt.html'
_template_uri = 'rental_return_receipt.html'
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
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        trans_date_in_updated = context.get('trans_date_in_updated', UNDEFINED)
        rental_items = context.get('rental_items', UNDEFINED)
        damage_fee_total = context.get('damage_fee_total', UNDEFINED)
        late_fee_total = context.get('late_fee_total', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        date_in = context.get('date_in', UNDEFINED)
        fee_total = context.get('fee_total', UNDEFINED)
        request = context.get('request', UNDEFINED)
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
        user = context.get('user', UNDEFINED)
        trans_date_in_updated = context.get('trans_date_in_updated', UNDEFINED)
        rental_items = context.get('rental_items', UNDEFINED)
        damage_fee_total = context.get('damage_fee_total', UNDEFINED)
        late_fee_total = context.get('late_fee_total', UNDEFINED)
        def content():
            return render_content(context)
        date_in = context.get('date_in', UNDEFINED)
        fee_total = context.get('fee_total', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<p style="font-weight: bold;">Hello ')
        __M_writer(str( user.get_full_name() ))
        __M_writer(',</p>\n<p>Thank you for renting from us!</p>\n<p>You returned your items on <b>')
        __M_writer(str( date_in.strftime('%b %d, %Y') ))
        __M_writer('</b></p>\n')
        if fee_total != '0.00':
            __M_writer('    <table class="table table-striped">\n        <tr>\n            <th>Rental Product</th>\n            <th>Damage Description</th>\n            <th>Damage Fee</th>\n            <th>Late Fee</th>\n        </tr>\n')
            for rental_item in rental_items:
                __M_writer('            <tr>\n                <td>')
                __M_writer(str( rental_item ))
                __M_writer('</td>\n')
                if rental_items[rental_item][2] != '':
                    __M_writer('                    <td>')
                    __M_writer(str( rental_items[rental_item][2] ))
                    __M_writer('</td>\n')
                else:
                    __M_writer('                    <td>N/A</td>\n')
                if rental_items[rental_item][1] != '':
                    __M_writer('                    <td>$')
                    __M_writer(str( rental_items[rental_item][1] ))
                    __M_writer('</td>\n')
                else:
                    __M_writer('                    <td>N/A</td>\n')
                if rental_items[rental_item][0] != '':
                    __M_writer('                    <td>$')
                    __M_writer(str( rental_items[rental_item][0] ))
                    __M_writer('</td>\n')
                else:
                    __M_writer('                    <td>N/A</td>\n')
                __M_writer('            </tr>\n')
            __M_writer('        <tr>\n            <td></td>\n            <td></td>\n            <td></td>\n            <td></td>\n        </tr>\n        <tr style="font-weight: bold;">\n            <td>')
            __M_writer(str( trans_date_in_updated.get_rental_item_count() ))
            __M_writer(' item(s)</td>\n            <td>Subtotal</td>\n            <td>$')
            __M_writer(str( damage_fee_total ))
            __M_writer('</td>\n            <td>$')
            __M_writer(str( late_fee_total ))
            __M_writer('</td>\n        </tr>\n        <tr style="font-weight: bold;">\n            <td></td>\n            <td>Total</td>\n            <td></td>\n            <td>$')
            __M_writer(str( fee_total ))
            __M_writer('</td>\n        </tr>\n        <tr style="font-weight: bold;">\n            <td></td>\n            <td></td>\n            <td>Payment</td>\n            <td>$')
            __M_writer(str( request.session['return_charge_resp']['Amount'] ))
            __M_writer(' ')
            __M_writer(str( request.session['return_charge_resp']['Currency'] ))
            __M_writer('</td>\n        </tr>\n    </table>\n')
        else:
            __M_writer('    <table class="table table-striped">\n        <tr>\n            <th>Rental Product</th>\n        </tr>\n')
            for rental_item in rental_items:
                __M_writer('            <tr>\n                <td>')
                __M_writer(str( rental_item ))
                __M_writer('</td>\n            </tr>\n')
            __M_writer('        <tr style="font-weight: bold;">\n            <td>')
            __M_writer(str( trans_date_in_updated.get_rental_item_count() ))
            __M_writer(' item(s)</td>\n        </tr>\n    </table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Nate/chf_dmp/homepage/templates/rental_return_receipt.html", "source_encoding": "ascii", "uri": "rental_return_receipt.html", "line_map": {"27": 0, "42": 1, "52": 3, "66": 3, "67": 4, "68": 4, "69": 6, "70": 6, "71": 7, "72": 8, "73": 15, "74": 16, "75": 17, "76": 17, "77": 18, "78": 19, "79": 19, "80": 19, "81": 20, "82": 21, "83": 23, "84": 24, "85": 24, "86": 24, "87": 25, "88": 26, "89": 28, "90": 29, "91": 29, "92": 29, "93": 30, "94": 31, "95": 33, "96": 35, "97": 42, "98": 42, "99": 44, "100": 44, "101": 45, "102": 45, "103": 51, "104": 51, "105": 57, "106": 57, "107": 57, "108": 57, "109": 60, "110": 61, "111": 65, "112": 66, "113": 67, "114": 67, "115": 70, "116": 71, "117": 71, "123": 117}}
__M_END_METADATA
"""
