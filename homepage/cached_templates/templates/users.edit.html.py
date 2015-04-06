# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423176611.114737
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/users.edit.html'
_template_uri = 'users.edit.html'
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
        form = context.get('form', UNDEFINED)
        request = context.get('request', UNDEFINED)

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
        form = context.get('form', UNDEFINED)
        request = context.get('request', UNDEFINED)

        def content():
            return render_content(context)

        __M_writer = context.writer()
        __M_writer(
            '\n\n    <form method="POST">\n        <div class="form-group">\n            <table>\n                ')
        __M_writer(str(form))
        __M_writer(
            '\n            </table>\n        </div>\n        <button class="btn btn-primary" type="submit">Save</button>\n\n')
        if request.urlparams[1] == 'new':
            __M_writer('          <a class="btn btn-primary" href="/homepage/users.delete/')
            __M_writer(str(request.urlparams[0]))
            __M_writer('/">Cancel</a>\n')
        else:
            __M_writer('          <a class="btn btn-primary" href="/homepage/users/">Cancel</a>\n')
        __M_writer('    </form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Nate/chf_dmp/homepage/templates/users.edit.html", "source_encoding": "ascii", "uri": "users.edit.html", "line_map": {"27": 0, "36": 1, "69": 63, "46": 3, "54": 3, "55": 8, "56": 8, "57": 13, "58": 14, "59": 14, "60": 14, "61": 15, "62": 16, "63": 18}}
__M_END_METADATA
"""
