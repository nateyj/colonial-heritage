# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428528412.849932
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/catalog/templates/product.html'
_template_uri = '/catalog/templates/product.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['title', 'content']


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
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
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


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\n<title>CHF - Products</title>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="text-left">\n    <h1 class="page-header">Products</h1>\n</div>\n<div id="search_results_container">\n    <div id="custom-search-input">\n        <div class="input-group col-md-3">\n            <input id="search" type="text" class="form-control" placeholder="Search">\n            <span class="input-group-btn">\n                <button id="search_btn" class="btn btn-primary" type="button">\n                    Clear <span class=" glyphicon glyphicon-search"></span>\n                </button>\n            </span>\n        </div>\n    </div>\n    <div id="search_results">\n')
        for product in products:
            __M_writer('        <div class="item_container">\n            <a href="/catalog/product.detail/')
            __M_writer(str( product.id ))
            __M_writer('">\n')
            if product.product_specification.photo is not None:
                __M_writer('                    <img src="')
                __M_writer(str( STATIC_URL ))
                __M_writer('catalog/media/images/product_pictures/')
                __M_writer(str( product.product_specification.photo.image ))
                __M_writer('"/>\n')
            else:
                __M_writer('                    No picture available\n')
            __M_writer('\n                <div class="text-muted text-center">')
            __M_writer(str( product.product_specification.name ))
            __M_writer('</div>\n            </a>\n\n            <div class="text-center">\n                <button data-product_id="')
            __M_writer(str( product.id ))
            __M_writer('" class="add_to_cart_btn btn btn-warning btn-xs">Add to Cart\n                </button>\n            </div>\n        </div>\n')
        __M_writer('    </div>\n    <!--search_results-->\n</div>  <!--search_results_container-->\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/catalog/templates/product.html", "source_encoding": "ascii", "filename": "/Users/Nate/chf_dmp/catalog/templates/product.html", "line_map": {"65": 7, "73": 7, "74": 24, "75": 25, "76": 26, "77": 26, "78": 27, "79": 28, "80": 28, "81": 28, "82": 28, "83": 28, "84": 29, "85": 30, "86": 32, "87": 33, "88": 33, "89": 37, "90": 37, "27": 0, "97": 91, "91": 42, "38": 1, "43": 5, "53": 3, "59": 3}}
__M_END_METADATA
"""
