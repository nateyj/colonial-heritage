# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428527544.604062
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/product.html'
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
def render_body(context,**pageargs):
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="text-left">\n    <h1>Products</h1>\n</div>\n\n<div class="text-left" style="margin-bottom: 20px;">\n    <a href="/homepage/product.edit/new/" class="btn btn-warning">Add New Product</a>\n</div>\n\n<table id="product_table" class="table table-striped">\n    <tr>\n        <th>Actions</th>\n        <th>ID</th>\n        <th>Name</th>\n        <th>Description</th>\n        <th>Category</th>\n        <th>Price</th>\n        <!--<th>Producer</th>-->\n    </tr>\n')
        for product in products:
            __M_writer('    <tr>\n        <td>\n            <a href="/homepage/product.edit/edit/')
            __M_writer(str( product.id ))
            __M_writer('/">Edit</a>\n            |\n            <a href="/homepage/product.delete/')
            __M_writer(str( product.id ))
            __M_writer('/">Delete</a>\n        </td>\n        <td>')
            __M_writer(str( product.id ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( product ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( product.product_specification.description ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( product.product_specification.category ))
            __M_writer('</td>\n        <td>$')
            __M_writer(str( product.product_specification.price ))
            __M_writer('</td>\n    </tr>\n')
        __M_writer('</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 32, "65": 33, "66": 33, "67": 34, "68": 34, "69": 37, "75": 69, "27": 0, "35": 1, "45": 3, "52": 3, "53": 23, "54": 24, "55": 26, "56": 26, "57": 28, "58": 28, "59": 30, "60": 30, "61": 31, "62": 31, "63": 32}, "filename": "/Users/Nate/chf_dmp/homepage/templates/product.html", "source_encoding": "ascii", "uri": "product.html"}
__M_END_METADATA
"""
