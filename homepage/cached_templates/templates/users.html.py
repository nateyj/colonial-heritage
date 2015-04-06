# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423363250.31605
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/users.html'
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
        users = context.get('users', UNDEFINED)

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
        users = context.get('users', UNDEFINED)

        def content():
            return render_content(context)

        __M_writer = context.writer()
        __M_writer(
            '\n\n<div>\n    <h1 class="page-header text-left">Users</h1>\n</div>\n\n<div class="text-left" style="margin-bottom: 20px;">\n    <a href="/homepage/users.create/" class="btn btn-warning">Add New User</a>\n</div>\n\n<table id="users_table" class="table table-striped">\n    <tr>\n        <th>Actions</th>\n        <th>ID</th>\n        <th>Authorization</th>\n        <th>First Name</th>\n        <th>Last Name</th>\n        <th>Username</th>\n        <th>Security Question</th>\n        <th>Email</th>\n        <th>Last Login</th>\n    </tr>\n')
        for user in users:
            __M_writer('        <tr>\n            <td>\n                <a href="/homepage/users.edit/')
            __M_writer(str(user.id))
            __M_writer('/">Edit</a>\n                |\n                <a href="/homepage/users.delete/')
            __M_writer(str(user.id))
            __M_writer('/">Delete</a>\n            </td>\n            <td>')
            __M_writer(str(user.id))
            __M_writer('</td>\n            <td>')
            __M_writer(str(user.get_group()))
            __M_writer('</td>\n            <td>')
            __M_writer(str(user.first_name))
            __M_writer('</td>\n            <td>')
            __M_writer(str(user.last_name))
            __M_writer('</td>\n            <td>')
            __M_writer(str(user.username))
            __M_writer('</td>\n            <td>')
            __M_writer(str(user.security_question))
            __M_writer('</td>\n            <td>')
            __M_writer(str(user.email))
            __M_writer('</td>\n            <td>')
            __M_writer(str(user.last_login.strftime('%b %d, %Y %I:%M %p')))
            __M_writer('</td>\n        </tr>\n')
        __M_writer('</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 34, "65": 35, "66": 35, "67": 36, "68": 36, "69": 37, "70": 37, "71": 38, "72": 38, "73": 39, "74": 39, "75": 42, "81": 75, "27": 0, "35": 1, "45": 3, "52": 3, "53": 25, "54": 26, "55": 28, "56": 28, "57": 30, "58": 30, "59": 32, "60": 32, "61": 33, "62": 33, "63": 34}, "source_encoding": "ascii", "filename": "/Users/Nate/chf_dmp/homepage/templates/users.html", "uri": "users.html"}
__M_END_METADATA
"""
