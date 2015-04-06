# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425177385.390867
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/account/templates/users.html'
_template_uri = 'users.html'
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
        user = context.get('user', UNDEFINED)

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
        user = context.get('user', UNDEFINED)

        def content():
            return render_content(context)

        __M_writer = context.writer()
        __M_writer(
            '\n\n<div>\n    <h1 class="page-header text-left">My Account</h1>\n</div>\n\n<table id="users_table" class="table table-striped">\n    <tr>\n        <td>First Name</td>\n        <td>')
        __M_writer(str(user.first_name))
        __M_writer('</td>\n    </tr>\n    <tr>\n        <td>Last Name</td>\n        <td>')
        __M_writer(str(user.last_name))
        __M_writer('</td>\n    </tr>\n    <tr>\n        <td>Username</td>\n        <td>')
        __M_writer(str(user.username))
        __M_writer('</td>\n    </tr>\n    <tr>\n        <td>Security Question</td>\n        <td>')
        __M_writer(str(user.security_question))
        __M_writer('</td>\n    </tr>\n    <tr>\n        <td>Security Answer</td>\n        <td>')
        __M_writer(str(user.security_answer))
        __M_writer('</td>\n    </tr>\n    <tr>\n        <td>Email</td>\n        <td>')
        __M_writer(str(user.email))
        __M_writer('</td>\n    </tr>\n</table>\n\n<div>\n    <a class="btn btn-primary" href="/account/users.edit/')
        __M_writer(str(user.id))
        __M_writer('/">Edit</a>\n    <a class="btn btn-primary" href="/account/users.delete/')
        __M_writer(str(user.id))
        __M_writer('/">Delete</a>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "users.html", "filename": "/Users/Nate/chf_dmp/account/templates/users.html", "line_map": {"64": 32, "65": 37, "66": 37, "35": 1, "68": 38, "74": 68, "45": 3, "27": 0, "67": 38, "52": 3, "53": 12, "54": 12, "55": 16, "56": 16, "57": 20, "58": 20, "59": 24, "60": 24, "61": 28, "62": 28, "63": 32}}
__M_END_METADATA
"""
