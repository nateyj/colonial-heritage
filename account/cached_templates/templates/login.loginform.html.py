# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425331302.933161
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/account/templates/base.loginform.html'
_template_uri = 'base.loginform.html'
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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)


def render_body(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)

        def content():
            return render_content(context._locals(__M_locals))

        form = context.get('form', UNDEFINED)
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

        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(
            '\n\n<form id="loginform" method=\'POST\' action="/account/login.loginform">\n    <div class="form-group">\n        <table>\n            ')
        __M_writer(str(form))
        __M_writer(
            '\n        </table>\n    </div>\n    <div class="form-group">\n        <button class="btn btn-primary" type="submit">Sign In</button>\n    </div>\n</form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "52": 3, "53": 8, "54": 8, "27": 0, "60": 54, "45": 3}, "source_encoding": "ascii", "uri": "base.loginform.html", "filename": "/Users/Nate/chf_dmp/account/templates/base.loginform.html"}
__M_END_METADATA
"""
