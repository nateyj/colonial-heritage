# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425761919.056515
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/catalog/templates/product_detail.html'
_template_uri = '/catalog/templates/product_detail.html'
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
    return runtime._inherit_from(context, '/catalog/templates/base.htm', _template_uri)


def render_body(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        product = context.get('product', UNDEFINED)

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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        product = context.get('product', UNDEFINED)

        def content():
            return render_content(context)

        __M_writer = context.writer()
        __M_writer('\n\n<div class="text-left">\n    <h1 class="page-header">')
        __M_writer(str(product.product_specification.name))
        __M_writer('</h1>\n</div>\n<div>\n    <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('catalog/media/images/product_pictures/')
        __M_writer(str(product.product_specification.photo.image))
        __M_writer('"/>\n</div>\n<div>\n    <span class="title">Description:</span><br>\n    ')
        __M_writer(str(product.product_specification.description))
        __M_writer('<br><br>\n</div>\n<div>\n    <span class="title">Price:</span> <span class="price">$')
        __M_writer(str(product.product_specification.price))
        __M_writer(
            '</span><br><br>\n</div>\n<div>\n    Quantity: <input id="qty" type="number" value="1">\n    <button data-product_id="')
        __M_writer(str(product.id))
        __M_writer('" id="detail_add_to_cart_btn" class="btn btn-warning">Add to Cart</button>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 16, "65": 20, "66": 20, "27": 0, "36": 1, "72": 66, "46": 3, "54": 3, "55": 6, "56": 6, "57": 9, "58": 9, "59": 9, "60": 9, "61": 13, "62": 13, "63": 16}, "source_encoding": "ascii", "filename": "/Users/Nate/chf_dmp/catalog/templates/product_detail.html", "uri": "/catalog/templates/product_detail.html"}
__M_END_METADATA
"""
