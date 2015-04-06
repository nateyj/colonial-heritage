# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428021798.352376
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/account/templates/account.html'
_template_uri = 'account.html'
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
    return runtime._inherit_from(context, '/account/templates/base.htm', _template_uri)


def render_body(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)

        def title():
            return render_title(context._locals(__M_locals))

        def content():
            return render_content(context._locals(__M_locals))

        user = context.get('user', UNDEFINED)
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

        __M_writer = context.writer()
        __M_writer('\n    <title>My Account</title>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)

        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(
            '\n\n    <div>\n        <h1>My Account</h1>\n    </div>\n    <div>\n        <a class="btn btn-primary" href="/account/account.edit/')
        __M_writer(str(user.id))
        __M_writer('/">Edit</a>\n        <a class="btn btn-primary" href="/account/password.edit/')
        __M_writer(str(user.id))
        __M_writer(
            '/">Change Password</a>\n    </div>\n    <table id="users_table" class="table table-striped">\n        <tr>\n            <td>First Name</td>\n            <td>')
        __M_writer(str(user.first_name))
        __M_writer('</td>\n\n        </tr>\n        <tr>\n            <td>Last Name</td>\n            <td>')
        __M_writer(str(user.last_name))
        __M_writer('</td>\n\n        </tr>\n        <tr>\n            <td>Username</td>\n            <td>')
        __M_writer(str(user.username))
        __M_writer('</td>\n\n        </tr>\n        <tr>\n            <td>Security Question</td>\n            <td>')
        __M_writer(str(user.security_question))
        __M_writer('</td>\n        </tr>\n        <tr>\n            <td>Security Answer</td>\n            <td>')
        __M_writer(str(user.security_answer))
        __M_writer('</td>\n        </tr>\n        <tr>\n            <td>Email</td>\n            <td>')
        __M_writer(str(user.email))
        __M_writer('</td>\n        </tr>\n        <tr>\n            <td>Phone</td>\n            ')
        user_phones = user.user_phones.all()

        __M_writer('\n')
        if user_phones != []:
            __M_writer('                <td>\n')
            for phone in user_phones:
                __M_writer('                        ')
                __M_writer(str(phone.number))
                __M_writer(' (')
                __M_writer(str(phone.type))
                __M_writer(')  <a href="/account/phone.edit/')
                __M_writer(str(phone.id))
                __M_writer('/">Edit</a>\n                        | <a href="/account/phone.delete/')
                __M_writer(str(phone.id))
                __M_writer('/">Delete</a><br>\n')
            __M_writer('                </td>\n')
        else:
            __M_writer('                <td>None</td>\n')
        __M_writer('        </tr>\n    </table>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 7, "101": 51, "71": 7, "72": 13, "73": 13, "74": 14, "75": 14, "76": 19, "77": 19, "78": 24, "79": 24, "80": 29, "81": 29, "82": 34, "83": 34, "84": 38, "85": 38, "86": 42, "87": 42, "88": 46, "90": 46, "27": 0, "92": 48, "93": 49, "94": 50, "95": 50, "96": 50, "97": 50, "98": 50, "91": 47, "100": 50, "37": 1, "102": 51, "103": 53, "104": 54, "105": 55, "42": 5, "99": 50, "52": 3, "112": 106, "58": 3, "106": 57}, "source_encoding": "ascii", "filename": "/Users/Nate/chf_dmp/account/templates/account.html", "uri": "account.html"}
__M_END_METADATA
"""
