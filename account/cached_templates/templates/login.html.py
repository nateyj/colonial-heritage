# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425331255.310434
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/account/templates/login.html'
_template_uri = 'login.html'
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


def render_body(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)

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
        def content():
            return render_content(context)

        __M_writer = context.writer()
        __M_writer(
            '\n\n<div id="login_dialog" class="modal fade">\n    <div class="modal-dialog">\n        <div class="modal-content">\n            <div class="modal-header">\n                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n                <h4 class="modal-title">Sign In</h4>\n            </div>\n            <div class="modal-body">\n                <p>One fine body&hellip;</p>\n            </div>\n            <div class="modal-footer">\n                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n                <button type="button" class="btn btn-primary">Sign In</button>\n            </div>\n        </div><!-- /.modal-content -->\n    </div><!-- /.modal-dialog -->\n</div><!-- /.modal -->\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "source_encoding": "ascii", "uri": "login.html", "filename": "/Users/Nate/chf_dmp/account/templates/login.html"}
__M_END_METADATA
"""
