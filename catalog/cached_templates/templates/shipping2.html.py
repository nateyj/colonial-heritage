# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427344139.012821
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/catalog/templates/shipping2.html'
_template_uri = 'shipping2.html'
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
    return runtime._inherit_from(context, '/account/templates/base.htm', _template_uri)


def render_body(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)

        def content():
            return render_content(context._locals(__M_locals))

        billing_form = context.get('billing_form', UNDEFINED)
        shipping_form = context.get('shipping_form', UNDEFINED)
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

        billing_form = context.get('billing_form', UNDEFINED)
        shipping_form = context.get('shipping_form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(
            '\n\n    <form method="POST">\n        <div>\n            <h2>Shipping Information</h2>\n        </div>\n        <table>\n            ')
        __M_writer(str(shipping_form))
        __M_writer(
            '\n        </table>\n        <br><br>\n\n        <div>\n            <h2>Billing Information</h2>\n        </div>\n        <table>\n            ')
        __M_writer(str(billing_form))
        __M_writer(
            '\n        </table>\n        <br><br>\n        <button class="submit_btn btn btn-primary" type="submit">Place Order</button>\n        <a class="btn btn-primary" href="/catalog/product/">Cancel</a>\n    </form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 58, "36": 1, "54": 3, "55": 10, "56": 10, "57": 18, "58": 18, "27": 0, "46": 3}, "uri": "shipping2.html", "filename": "/Users/Nate/chf_dmp/catalog/templates/shipping2.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
