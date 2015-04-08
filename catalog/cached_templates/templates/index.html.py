# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428530273.003749
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/catalog/templates/index.html'
_template_uri = 'index.html'
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
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        now = context.get('now', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        now = context.get('now', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="content">\n    <h3>Congratulations -- you\'ve successfully created a new django-mako-plus app!</h3>\n    <p>\n        The Colonial Heritage Foundation (the Foundation) is a 501(c)(3) corporation dedicated to the preservation o\n        the values, culture, skills and history of America\'s founding. To accomplish this mission, the Foundation engage\n        in a broad array of activities. Among these are the development and presentation of educational exhibits, the\n        coordination of reading and discussion groups to encourage the study of America\'s historical writings, the\n        presentation of lectures and seminars regarding America\'s founding era, the coordination of historical\n        reenactments and skill demonstrations, and the coordination of internships and apprenticeships that teach the\n        occupational skills of early America.\n    </p>\n\n    <!--<p class="server-time">The current server time is ')
        __M_writer(str( now ))
        __M_writer('</p>\n    <button id="server-time-button" class="btn btn-primary">Refresh Server Time</button>\n    <p class="browser-time">The current browser time is...</p><-->\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/Nate/chf_dmp/catalog/templates/index.html", "uri": "index.html", "line_map": {"35": 1, "52": 3, "53": 16, "54": 16, "27": 0, "60": 54, "45": 3}}
__M_END_METADATA
"""
