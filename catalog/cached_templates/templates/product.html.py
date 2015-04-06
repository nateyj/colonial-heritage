# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425175328.44432
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/account/templates/product.html'
_template_uri = 'product.html'
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

        def content():
            return render_content(context._locals(__M_locals))

        products = context.get('products', UNDEFINED)
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

        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(
            '\n\n<div class="text-left">\n    <h1 class="page-header">Products</h1>\n</div>\n\n<table id="product_table" class="table table-striped">\n    <tr>\n        <th>Name</th>\n        <th>Description</th>\n        <th>Category</th>\n        <th>Current Price</th>\n    </tr>\n')
        for product in products:
            __M_writer('        <tr>\n            <td>')
            __M_writer(str(product.name))
            __M_writer('</td>\n            <td>')
            __M_writer(str(product.description))
            __M_writer('</td>\n            <td>')
            __M_writer(str(product.category))
            __M_writer('</td>\n            <td>$ ')
            __M_writer(str(product.current_price))
            __M_writer('</td>\n        </tr>\n')
        __M_writer('</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Nate/chf_dmp/account/templates/product.html", "uri": "product.html", "line_map": {"35": 1, "69": 63, "45": 3, "27": 0, "52": 3, "53": 16, "54": 17, "55": 18, "56": 18, "57": 19, "58": 19, "59": 20, "60": 20, "61": 21, "62": 21, "63": 24}, "source_encoding": "ascii"}
__M_END_METADATA
"""
