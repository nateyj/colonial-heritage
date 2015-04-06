# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423366199.275846
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/event.html'
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
            '\n\n<div class="text-left">\n    <h1 class="page-header">Events</h1>\n</div>\n\n<div class="text-left" style="margin-bottom: 20px;">\n    <a href="/homepage/event.create/" class="btn btn-warning">Add New Event</a>\n</div>\n\n<table id="event_table" class="table table-striped">\n    <tr>\n        <th>Actions</th>\n        <th>ID</th>\n        <th>Name</th>\n        <th>Start Date</th>\n        <th>End Date</th>\n        <th>Map File Name</th>\n    </tr>\n')
        for event in events:
            __M_writer('        <tr>\n            <td>\n                <a href="/homepage/event.edit/')
            __M_writer(str(event.id))
            __M_writer('/">Edit</a>\n                |\n                <a href="/homepage/event.delete/')
            __M_writer(str(event.id))
            __M_writer('/">Delete</a>\n            </td>\n            <td>')
            __M_writer(str(event.id))
            __M_writer('</td>\n            <td>')
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
{"filename": "/Users/Nate/chf_dmp/homepage/templates/event.html", "source_encoding": "ascii", "uri": "event.html", "line_map": {"64": 31, "65": 32, "66": 32, "67": 33, "68": 33, "69": 36, "75": 69, "27": 0, "35": 1, "45": 3, "52": 3, "53": 22, "54": 23, "55": 25, "56": 25, "57": 27, "58": 27, "59": 29, "60": 29, "61": 30, "62": 30, "63": 31}}
__M_END_METADATA
"""
