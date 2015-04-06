# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428056956.917875
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/rental_order_confirmation.html'
_template_uri = 'rental_order_confirmation.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)


def render_body(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)

        def title():
            return render_title(context._locals(__M_locals))

        def content():
            return render_content(context._locals(__M_locals))

        user = context.get('user', UNDEFINED)
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


def render_title(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)

        __M_writer = context.writer()
        __M_writer('\n    <title>Thanks for Your Bank</title>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)

        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <h1>Thank you for renting from us ')
        __M_writer(str(user.get_full_name()))
        __M_writer('!</h1>\n    <p>A confirmation email has been sent to you.</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "rental_order_confirmation.html", "line_map": {"64": 7, "52": 3, "37": 1, "71": 7, "72": 8, "73": 8, "58": 3, "27": 0, "42": 5, "79": 73}, "filename": "/Users/Nate/chf_dmp/homepage/templates/rental_order_confirmation.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
