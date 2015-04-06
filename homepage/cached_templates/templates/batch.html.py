# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428142833.472062
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/batch.html'
_template_uri = 'batch.html'
_source_encoding = 'ascii'
import os, os.path, re

_exports = ['content', 'title']


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

        def content():
            return render_content(context._locals(__M_locals))

        over90_days_overdue_dict = context.get('over90_days_overdue_dict', UNDEFINED)

        def title():
            return render_title(context._locals(__M_locals))

        thirtyTo60_customers_dict = context.get('thirtyTo60_customers_dict', UNDEFINED)
        sixtyTo90_customers_dict = context.get('sixtyTo90_customers_dict', UNDEFINED)
        thirtyTo60_days_overdue_dict = context.get('thirtyTo60_days_overdue_dict', UNDEFINED)
        sixtyTo90_days_overdue_dict = context.get('sixtyTo90_days_overdue_dict', UNDEFINED)
        over90_customers_dict = context.get('over90_customers_dict', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)

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

        over90_days_overdue_dict = context.get('over90_days_overdue_dict', UNDEFINED)
        thirtyTo60_customers_dict = context.get('thirtyTo60_customers_dict', UNDEFINED)
        sixtyTo90_customers_dict = context.get('sixtyTo90_customers_dict', UNDEFINED)
        thirtyTo60_days_overdue_dict = context.get('thirtyTo60_days_overdue_dict', UNDEFINED)
        over90_customers_dict = context.get('over90_customers_dict', UNDEFINED)
        sixtyTo90_days_overdue_dict = context.get('sixtyTo90_days_overdue_dict', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(
            '\n\n<div class="text-left">\n    <h1 class="page-header">Overdue Rental Items</h1>\n</div>\n\n<a href="/homepage/report.overdue_email/" class="btn btn-primary">Send Reminder Emails</a>\n\n<div>\n')
        if thirtyTo60_customers_dict != {}:
            __M_writer(
                '        <h2>Rental Transactions 30-59 Days Overdue</h2>\n        <table class="table table-striped">\n            <tr>\n                <th>Customer</th>\n                <th>Days Overdue</th>\n                <th>Rental Products</th>\n            </tr>\n')
            for customer in thirtyTo60_customers_dict:
                for transaction in thirtyTo60_customers_dict[customer]:
                    __M_writer('                    <tr>\n                        <td>')
                    __M_writer(str(customer.get_full_name()))
                    __M_writer('</td>\n                        <td>')
                    __M_writer(str(thirtyTo60_days_overdue_dict[customer][transaction]))
                    __M_writer('</td>\n                        <td>\n')
                    for rental_item in thirtyTo60_customers_dict[customer][transaction]:
                        __M_writer('                                ')
                        __M_writer(str(rental_item))
                        __M_writer('<br/>\n')
                    __M_writer('                        </td>\n                    </tr>\n')
            __M_writer('        </table>\n')
        else:
            __M_writer('        <h2>No Rental Transactions 30-60 Days Overdue</h2>\n')
        __M_writer('</div>\n<div>\n')
        if sixtyTo90_customers_dict != {}:
            __M_writer(
                '        <h2>Rental Transactions 60-89 Days Overdue</h2>\n        <table class="table table-striped">\n            <tr>\n                <th>Customer</th>\n                <th>Days Overdue</th>\n                <th>Rental Products</th>\n            </tr>\n')
            for customer in sixtyTo90_customers_dict:
                for transaction in sixtyTo90_customers_dict[customer]:
                    __M_writer('                    <tr>\n                        <td>')
                    __M_writer(str(customer.get_full_name()))
                    __M_writer('</td>\n                        <td>')
                    __M_writer(str(sixtyTo90_days_overdue_dict[customer][transaction]))
                    __M_writer('</td>\n                        <td>\n')
                    for rental_item in sixtyTo90_customers_dict[customer][transaction]:
                        __M_writer('                                ')
                        __M_writer(str(rental_item))
                        __M_writer('<br/>\n')
                    __M_writer('                        </td>\n                    </tr>\n')
            __M_writer('        </table>\n')
        else:
            __M_writer('        <h2>No Rental Transactions 30-59 Days Overdue</h2>\n')
        __M_writer('</div>\n<div>\n')
        if over90_customers_dict != {}:
            __M_writer(
                '        <h2>Rental Transactions Over 89 Days Overdue</h2>\n        <table class="table table-striped">\n            <tr>\n                <th>Customer</th>\n                <th>Days Overdue</th>\n                <th>Rental Products</th>\n            </tr>\n')
            for customer in over90_customers_dict:
                for transaction in over90_customers_dict[customer]:
                    __M_writer('                    <tr>\n                        <td>')
                    __M_writer(str(customer.get_full_name()))
                    __M_writer('</td>\n                        <td>')
                    __M_writer(str(over90_days_overdue_dict[customer][transaction]))
                    __M_writer('</td>\n                        <td>\n')
                    for rental_item in over90_customers_dict[customer][transaction]:
                        __M_writer('                                ')
                        __M_writer(str(rental_item))
                        __M_writer('<br/>\n')
                    __M_writer('                        </td>\n                    </tr>\n')
            __M_writer('        </table>\n')
        else:
            __M_writer('        <h2>No Rental Transactions Over 89 Days Overdue</h2>\n')
        __M_writer('</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)

        __M_writer = context.writer()
        __M_writer('\n    <title>CHF - Reports</title>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"129": 3, "135": 3, "141": 135, "27": 0, "42": 1, "47": 5, "57": 7, "69": 7, "70": 16, "71": 17, "72": 24, "73": 25, "74": 26, "75": 27, "76": 27, "77": 28, "78": 28, "79": 30, "80": 31, "81": 31, "82": 31, "83": 33, "84": 37, "85": 38, "86": 39, "87": 41, "88": 43, "89": 44, "90": 51, "91": 52, "92": 53, "93": 54, "94": 54, "95": 55, "96": 55, "97": 57, "98": 58, "99": 58, "100": 58, "101": 60, "102": 64, "103": 65, "104": 66, "105": 68, "106": 70, "107": 71, "108": 78, "109": 79, "110": 80, "111": 81, "112": 81, "113": 82, "114": 82, "115": 84, "116": 85, "117": 85, "118": 85, "119": 87, "120": 91, "121": 92, "122": 93, "123": 95}, "uri": "batch.html", "source_encoding": "ascii", "filename": "/Users/Nate/chf_dmp/homepage/templates/batch.html"}
__M_END_METADATA
"""
