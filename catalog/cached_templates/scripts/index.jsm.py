# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426544011.476607
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/catalog/scripts/index.jsm'
_template_uri = 'index.jsm'
_source_encoding = 'ascii'
import os, os.path, re

_exports = []


def render_body(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(
            "$(function() {\n    // update the time every 1 seconds\n    window.setInterval(function() {\n        $('.browser-time').text('The current browser time is ' + new Date() + '.');\n    },  ")
        __M_writer(str(request.urlparams[1] or 1000))
        __M_writer(
            ");\n\n    // update button\n    $('#server-time-button').click(function() {\n        $('.server-time').load('/catalog/index.get_time');\n    });\n});\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Nate/chf_dmp/catalog/scripts/index.jsm", "source_encoding": "ascii", "uri": "index.jsm", "line_map": {"16": 0, "24": 5, "30": 24, "22": 1, "23": 5}}
__M_END_METADATA
"""
