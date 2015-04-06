# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425518860.414251
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/account/templates/base.htm'
_template_uri = '/account/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re

_exports = []


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
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/account/templates/base.htm", "line_map": {"27": 0, "37": 27}, "source_encoding": "ascii", "filename": "/Users/Nate/chf_dmp/account/templates/base.htm"}
__M_END_METADATA
"""
