# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428125751.498318
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/overdue_reminder.html'
_template_uri = 'overdue_reminder.html'
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

        def content():
            return render_content(context._locals(__M_locals))

        days_overdue = context.get('days_overdue', UNDEFINED)
        overdue_items = context.get('overdue_items', UNDEFINED)
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
        def content():
            return render_content(context)

        days_overdue = context.get('days_overdue', UNDEFINED)
        overdue_items = context.get('overdue_items', UNDEFINED)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <p style="font-weight: bold;">Hello ')
        __M_writer(str(user.get_full_name()))
        __M_writer(
            ',</p>\n    <p>You have items that are past due. Please get off the couch and return them!</p>\n    <table>\n        <tr>\n            <th>Rental Product</th>\n            <th>Date Out</th>\n            <th>Date Due</th>\n            <th>Days Overdue</th>\n            <th>Late Fee Price Per Day</th>\n            <th>Amount</th>\n        </tr>\n        <tr>\n            <td></td>\n            <td></td>\n            <td></td>\n            <td></td>\n        </tr>\n')
        for rental_item in overdue_items:
            __M_writer('            <tr>\n                <td>')
            __M_writer(str(rental_item.rental_product.product_specification.name))
            __M_writer('</td>\n                <td>')
            __M_writer(str(overdue_items[rental_item][2].date.strftime('%b %d, %Y')))
            __M_writer('</td>\n                <td>')
            __M_writer(str(rental_item.date_due.strftime('%b %d, %Y')))
            __M_writer('</td>\n                <td>')
            __M_writer(str(days_overdue))
            __M_writer('</td>\n                <td>$')
            __M_writer(str(overdue_items[rental_item][0]))
            __M_writer('</td>\n                <td>$')
            __M_writer(str(overdue_items[rental_item][1]))
            __M_writer('</td>\n            </tr>\n')
        __M_writer('    </table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "overdue_reminder.html", "filename": "/Users/Nate/chf_dmp/homepage/templates/overdue_reminder.html", "line_map": {"64": 24, "65": 25, "66": 25, "67": 26, "68": 26, "69": 27, "70": 27, "71": 28, "72": 28, "73": 31, "79": 73, "27": 0, "37": 1, "47": 3, "56": 3, "57": 4, "58": 4, "59": 21, "60": 22, "61": 23, "62": 23, "63": 24}, "source_encoding": "ascii"}
__M_END_METADATA
"""
