# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428210864.385142
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/catalog/templates/event.html'
_template_uri = 'event.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)


def render_body(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)

        def title():
            return render_title(context._locals(__M_locals))

        def content():
            return render_content(context._locals(__M_locals))

        public_event_photo = context.get('public_event_photo', UNDEFINED)
        public_event = context.get('public_event', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        event = context.get('event', UNDEFINED)
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

        public_event = context.get('public_event', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <title>')
        __M_writer(str(public_event.name))
        __M_writer('</title>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)

        def content():
            return render_content(context)

        public_event_photo = context.get('public_event_photo', UNDEFINED)
        public_event = context.get('public_event', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        event = context.get('event', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n    <div id="festival_info">\n        <h1 class="page-header">')
        __M_writer(str(public_event.name))
        __M_writer('</h1>\n        <h4>Dates: ')
        __M_writer(str(event.start_date.strftime('%b %d, %Y')))
        __M_writer(' - ')
        __M_writer(str(event.end_date.strftime('%b %d, %Y')))
        __M_writer('</h4>\n        <img id="festival" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('catalog/media/images/festival/')
        __M_writer(str(public_event_photo.image))
        __M_writer('"/>\n        <br/><br/>\n        <p>')
        __M_writer(str(public_event.description))
        __M_writer('</p>\n    </div>\n    <h3>Areas</h3>\n    <div>\n')
        for area in areas:
            __M_writer('            <div class="item_container">\n                <img src="')
            __M_writer(str(STATIC_URL))
            __M_writer('catalog/media/images/area/')
            __M_writer(str(area.area_photos.all()[0].image))
            __M_writer('"/>\n                <div class="area-name text-muted text-center">')
            __M_writer(str(area.name))
            __M_writer(
                '</div>\n                <div class="text-center">\n                    <a href="/catalog/event.area_detail/')
            __M_writer(str(area.name))
            __M_writer('" class="btn btn-success">View Details</a>\n                </div>\n            </div>\n')
        __M_writer('    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 4, "65": 4, "71": 7, "82": 7, "83": 10, "84": 10, "85": 11, "86": 11, "87": 11, "88": 11, "89": 12, "90": 12, "91": 12, "92": 12, "93": 14, "94": 14, "95": 18, "96": 19, "97": 20, "98": 20, "27": 0, "100": 20, "101": 21, "102": 21, "103": 23, "104": 23, "41": 1, "46": 5, "111": 105, "99": 20, "105": 27, "56": 3, "63": 3}, "filename": "/Users/Nate/chf_dmp/catalog/templates/event.html", "uri": "event.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
