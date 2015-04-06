# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427324620.211898
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/catalog/templates/checkout.html'
_template_uri = 'checkout.html'
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

        def content():
            return render_content(context._locals(__M_locals))

        request = context.get('request', UNDEFINED)
        billing_form = context.get('billing_form', UNDEFINED)
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

        request = context.get('request', UNDEFINED)
        billing_form = context.get('billing_form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if request.user.is_authenticated():
            __M_writer(
                '        <div class="content">\n          <h1>Checkout</h1>\n        </div>\n        <form method="POST">\n            <div>Billing Information<br><br></div>\n            <table>\n                ')
            __M_writer(str(billing_form))
            __M_writer(
                '\n            </table><br><br>\n            <button id="place_order" type="submit" class="btn btn-warning">Place Order</button>\n            <a href="/catalog/product/" class="btn btn-primary">Cancel</a>\n        </form>\n')
        else:
            __M_writer('        <div>You must have an account and be logged in to checkout.</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/Nate/chf_dmp/catalog/templates/checkout.html", "line_map": {"66": 60, "59": 16, "36": 1, "54": 3, "55": 4, "56": 5, "57": 11, "58": 11, "27": 0, "60": 17, "46": 3}, "uri": "checkout.html"}
__M_END_METADATA
"""
