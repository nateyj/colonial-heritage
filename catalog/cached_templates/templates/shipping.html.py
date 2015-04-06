# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427339719.429417
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/catalog/templates/shipping.html'
_template_uri = 'shipping.html'
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
        user = context.get('user', UNDEFINED)
        phone = context.get('phone', UNDEFINED)
        address = context.get('address', UNDEFINED)

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
        user = context.get('user', UNDEFINED)
        phone = context.get('phone', UNDEFINED)
        address = context.get('address', UNDEFINED)

        def content():
            return render_content(context)

        __M_writer = context.writer()
        __M_writer(
            '\n\n    <div>\n        <h1>Shipping Information</h1>\n    </div>\n\n    <div class="text-left">\n        <a href="/catalog/shipping.create/">Ship to New Address</a>\n        |\n        <a href="#">Change Address</a>\n        |\n        <a href="/homepage/shipping.edit/')
        __M_writer(str(user.id))
        __M_writer('/')
        __M_writer(str(address.id))
        __M_writer('/">Edit Address</a>\n    </div>\n    <div>\n        ')
        __M_writer(str(user.first_name))
        __M_writer(' ')
        __M_writer(str(user.last_name))
        __M_writer('<br>\n        ')
        __M_writer(str(address.address1))
        __M_writer(' ')
        __M_writer(str(address.address2))
        __M_writer('<br>\n        ')
        __M_writer(str(address.city))
        __M_writer(', ')
        __M_writer(str(address.state))
        __M_writer(' ')
        __M_writer(str(address.zip_code))
        __M_writer('<br>\n        ')
        __M_writer(str(address.country))
        __M_writer('<br>\n        ')
        __M_writer(str(phone.number))
        __M_writer(' <a href="/account/phone.edit/')
        __M_writer(str(phone.id))
        __M_writer('/">Edit</a>\n        | <a href="/account/phone.change/')
        __M_writer(str(user.id))
        __M_writer('/">Change</a>\n    </div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 17, "65": 18, "66": 18, "67": 18, "68": 18, "69": 19, "70": 19, "71": 19, "72": 19, "73": 19, "74": 19, "75": 20, "76": 20, "77": 21, "78": 21, "79": 21, "80": 21, "81": 22, "82": 22, "88": 82, "27": 0, "37": 1, "47": 3, "56": 3, "57": 14, "58": 14, "59": 14, "60": 14, "61": 17, "62": 17, "63": 17}, "uri": "shipping.html", "source_encoding": "ascii", "filename": "/Users/Nate/chf_dmp/catalog/templates/shipping.html"}
__M_END_METADATA
"""
