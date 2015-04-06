# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426713591.274403
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/catalog/templates/base.htm'
_template_uri = '/catalog/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re

_exports = ['nav']


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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)


def render_body(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)

        def nav():
            return render_nav(context._locals(__M_locals))

        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav'):
            context['self'].nav(**pageargs)

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def nav():
            return render_nav(context)

        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(
            '\n\n    <div id="outside_nav">\n      <nav class="navbar navbar-inverse">\n          <div id="inside_navbar" class="container-fluid">\n            <ul class="nav navbar-nav">\n                <li role="presentation" ')
        __M_writer(str('class="active"' if request.dmp_router_page == 'index' else ''))
        __M_writer(
            '>\n                    <a href="/catalog/index">Home</a>\n                </li>\n                <li role="presentation" ')
        __M_writer(str('class="active"' if request.dmp_router_page == 'product' else ''))
        __M_writer(
            '>\n                    <a href="/catalog/product">Products</a>\n                </li>\n                <li role="presentation" ')
        __M_writer(str('class="active"' if request.dmp_router_page == 'event' else ''))
        __M_writer(
            '>\n                    <a href="/catalog/event">Events</a>\n                </li>\n            </ul>\n            <ul id="navbar_right" class="nav navbar-nav navbar-right">\n')
        if request.user.is_authenticated():
            __M_writer('                    <p class="navbar-text">Welcome, ')
            __M_writer(str(request.user.first_name))
            __M_writer('!</p>\n                    <li role="presentation" ')
            __M_writer(str('class="active"' if request.dmp_router_page == 'account' else ''))
            __M_writer(
                '>\n                        <a href="/account/account">My Account</a>\n                    </li>\n                    <button type="button" id="view_cart" class="btn btn-warning navbar-btn">\n                        View Cart <span class="glyphicon glyphicon-shopping-cart" aria-hidden="true"></span>\n                    </button>\n                    <a href="/account/index2.logout_view/" class="btn btn-warning navbar-btn">Sign Out</a>\n')
        else:
            __M_writer(
                '                    <button id="show_login_dialog_nav" type="button" class="btn btn-warning navbar-btn">Sign In</button>\n                    <a href="/account/account.create/" class="btn btn-warning navbar-btn">Create Account</a>\n')
        __M_writer('            </ul>\n          </div>\n      </nav>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 22, "65": 29, "66": 30, "35": 1, "73": 67, "45": 3, "27": 0, "67": 33, "52": 3, "53": 9, "54": 9, "55": 12, "56": 12, "57": 15, "58": 15, "59": 20, "60": 21, "61": 21, "62": 21, "63": 22}, "source_encoding": "ascii", "filename": "/Users/Nate/chf_dmp/catalog/templates/base.htm", "uri": "/catalog/templates/base.htm"}
__M_END_METADATA
"""
