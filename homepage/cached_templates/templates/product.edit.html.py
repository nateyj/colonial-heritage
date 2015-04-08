# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428525522.837325
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/product.edit.html'
_template_uri = 'product.edit.html'
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
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
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
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<form method="POST">\n    <div class="form-group">\n        <table>\n            ')
        __M_writer(str( form ))
        __M_writer('\n        </table>\n    </div>\n')
        if request.urlparams[0] == 'new':
            __M_writer('        <button class="btn btn-primary" type="submit">Create</button>\n')
        else:
            __M_writer('        <button class="btn btn-primary" type="submit">Save</button>\n')
        __M_writer('    <a class="btn btn-primary" href="/homepage/product/">Cancel</a>\n</form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"27": 0, "36": 1, "46": 3, "67": 61, "54": 3, "55": 8, "56": 8, "57": 11, "58": 12, "59": 13, "60": 14, "61": 16}, "filename": "/Users/Nate/chf_dmp/homepage/templates/product.edit.html", "uri": "product.edit.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
