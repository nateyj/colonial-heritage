# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428211369.87539
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/catalog/templates/area_detail.html'
_template_uri = 'area_detail.html'
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
    return runtime._inherit_from(context, '/catalog/templates/base.htm', _template_uri)


def render_body(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)

        def title():
            return render_title(context._locals(__M_locals))

        area = context.get('area', UNDEFINED)

        def content():
            return render_content(context._locals(__M_locals))

        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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

        area = context.get('area', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <title>')
        __M_writer(str(area.public_event.name))
        __M_writer(' - ')
        __M_writer(str(area.name))
        __M_writer('</title>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        area = context.get('area', UNDEFINED)

        def content():
            return render_content(context)

        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div id="area_info">\n        <h1 class="page-header">')
        __M_writer(str(area.name))
        __M_writer(
            '</h1>\n        <a href="/catalog/event/" class="btn btn-warning pull-right">Back to Event</a>\n        <img id="area_img" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('catalog/media/images/area/')
        __M_writer(str(area.area_photos.all()[0].image))
        __M_writer('"/>\n        <br/><br/>\n        <p>')
        __M_writer(str(area.description))
        __M_writer('</p>\n    </div>\n    <h3>Items for Sale</h3>\n    <div>\n')
        for item in area.artisan_items.all():
            __M_writer('            <div class="item_container">\n                <img src="')
            __M_writer(str(STATIC_URL))
            __M_writer('catalog/media/images/artisan_item/')
            __M_writer(str(item.artisan_item_photos.all()[0].image))
            __M_writer('"/>\n                <div class="item-info text-muted text-center">')
            __M_writer(str(item.name))
            __M_writer('</div>\n                <div class="item-info text-muted text-center">$')
            __M_writer(str(item.price))
            __M_writer('</div>\n            </div>\n')
        __M_writer('    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 4, "70": 7, "78": 7, "79": 9, "80": 9, "81": 11, "82": 11, "83": 11, "84": 11, "85": 13, "86": 13, "87": 17, "88": 18, "89": 19, "90": 19, "27": 0, "92": 19, "93": 20, "94": 20, "95": 21, "96": 21, "97": 24, "91": 19, "38": 1, "103": 97, "43": 5, "53": 3, "60": 3, "61": 4, "62": 4, "63": 4}, "filename": "/Users/Nate/chf_dmp/catalog/templates/area_detail.html", "uri": "area_detail.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
