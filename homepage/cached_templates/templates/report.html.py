# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425782157.361258
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/report.html'
_template_uri = 'report.html'
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
        report = context.get('report', UNDEFINED)

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
        report = context.get('report', UNDEFINED)

        def content():
            return render_content(context)

        __M_writer = context.writer()
        __M_writer(
            '\n\n<div class="text-left">\n    <h1 class="page-header">Overdue Rental Items</h1>\n</div>\n\n<table id="event_table" class="table table-striped">\n    <tr>\n        <th>ID</th>\n        <th>Name</th>\n        <th>Due Date</th>\n    </tr>\n')
        for item in report:
            __M_writer('        <tr>\n            <td>')
            __M_writer(str(item.rental_product.id))
            __M_writer('</td>\n            <td>')
            __M_writer(str(item.rental_product.product_specification.name))
            __M_writer('</td>\n            <td>')
            __M_writer(str(item.date_due.strftime('%b %d, %Y')))
            __M_writer('</td>\n        </tr>\n')
        __M_writer('</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "report.html", "line_map": {"35": 1, "45": 3, "27": 0, "67": 61, "52": 3, "53": 15, "54": 16, "55": 17, "56": 17, "57": 18, "58": 18, "59": 19, "60": 19, "61": 22}, "filename": "/Users/Nate/chf_dmp/homepage/templates/report.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
