# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428633839.459732
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/account/templates/account.edit.html'
_template_uri = 'account.edit.html'
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
    return runtime._inherit_from(context, '/account/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<form method="POST">\n    <table>\n        ')
        __M_writer(str( form ))
        __M_writer('\n    </table>\n\n')
        if request.urlparams[0] == 'new':
            __M_writer('        <button data-site_user_id="" class="submit_btn btn btn-primary" type="submit">Create</button>\n')
        else:
            __M_writer('        <button data-site_user_id="')
            __M_writer(str( request.urlparams[1] ))
            __M_writer('" class="submit_btn btn btn-primary" type="submit">Save</button>\n')
        __M_writer('\n    <a class="btn btn-primary" href="/account/account/">Cancel</a>\n</form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"27": 0, "36": 1, "69": 63, "46": 3, "54": 3, "55": 7, "56": 7, "57": 10, "58": 11, "59": 12, "60": 13, "61": 13, "62": 13, "63": 15}, "filename": "/Users/Nate/chf_dmp/account/templates/account.edit.html", "uri": "account.edit.html"}
__M_END_METADATA
"""
