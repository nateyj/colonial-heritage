# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425175761.874088
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/account/templates/event.html'
_template_uri = 'event.html'
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


def render_body(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        events = context.get('events', UNDEFINED)

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
        events = context.get('events', UNDEFINED)

        def content():
            return render_content(context)

        __M_writer = context.writer()
        __M_writer(
            '\n\n<div class="text-left">\n    <h1 class="page-header">Events</h1>\n</div>\n\n<table id="event_table" class="table table-striped">\n    <tr>\n        <th>Name</th>\n        <th>Start Date</th>\n        <th>End Date</th>\n        <th>Map File Name</th>\n    </tr>\n')
        for event in events:
            __M_writer('        <tr>\n            <td>')
            __M_writer(str(event.name))
            __M_writer('</td>\n            <td>')
            __M_writer(str(event.start_date.strftime('%b %d, %Y')))
            __M_writer('</td>\n            <td>')
            __M_writer(str(event.end_date.strftime('%b %d, %Y')))
            __M_writer('</td>\n            <td>')
            __M_writer(str(event.map_file_name))
            __M_writer('</td>\n        </tr>\n')
        __M_writer('</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "event.html", "filename": "/Users/Nate/chf_dmp/account/templates/event.html", "line_map": {"35": 1, "69": 63, "45": 3, "27": 0, "52": 3, "53": 16, "54": 17, "55": 18, "56": 18, "57": 19, "58": 19, "59": 20, "60": 20, "61": 21, "62": 21, "63": 24}}
__M_END_METADATA
"""
