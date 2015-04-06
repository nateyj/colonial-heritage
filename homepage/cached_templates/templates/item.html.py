# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423364485.791546
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/item.html'
_template_uri = 'item.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)


def render_body(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        items = context.get('items', UNDEFINED)

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
        items = context.get('items', UNDEFINED)

        def content():
            return render_content(context)

        __M_writer = context.writer()
        __M_writer(
            '\n\n<div class="text-left">\n    <h1 class="page-header">Items</h1>\n</div>\n\n<div class="text-left" style="margin-bottom: 20px;">\n    <a href="/homepage/item.create/" class="btn btn-warning">Add New Item</a>\n</div>\n<table id="item_table" class="table table-striped">\n    <tr>\n        <th>Actions</th>\n        <th>ID</th>\n        <th>Name</th>\n        <th>Description</th>\n        <th>Value</th>\n        <th>Rentable</th>\n        <th>Owner</th>\n    </tr>\n')
        for item in items:
            __M_writer('        <tr>\n            <td>\n                <a href="/homepage/item.edit/')
            __M_writer(str(item.id))
            __M_writer('/">Edit</a>\n                |\n                <a href="/homepage/item.delete/')
            __M_writer(str(item.id))
            __M_writer('/">Delete</a>\n            </td>\n            <td>')
            __M_writer(str(item.id))
            __M_writer('</td>\n            <td>')
            __M_writer(str(item.name))
            __M_writer('</td>\n            <td>')
            __M_writer(str(item.description))
            __M_writer('</td>\n            <td>$ ')
            __M_writer(str(item.value))
            __M_writer('</td>\n            <td>')
            __M_writer(str(item.is_rentable))
            __M_writer('</td>\n            <td>')
            __M_writer(str(item.owner.given_name))
            __M_writer(' </td>\n        </tr>\n')
        __M_writer('</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 31, "65": 32, "66": 32, "67": 33, "68": 33, "69": 34, "70": 34, "71": 37, "77": 71, "27": 0, "35": 1, "45": 3, "52": 3, "53": 22, "54": 23, "55": 25, "56": 25, "57": 27, "58": 27, "59": 29, "60": 29, "61": 30, "62": 30, "63": 31}, "uri": "item.html", "filename": "/Users/Nate/chf_dmp/homepage/templates/item.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
