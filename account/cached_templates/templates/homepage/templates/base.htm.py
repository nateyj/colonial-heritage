# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428021708.574831
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re

_exports = ['title', 'content', 'nav']

from django_mako_plus.controller import static_files


def render_body(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)

        def title():
            return render_title(context._locals(__M_locals))

        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)

        def content():
            return render_content(context._locals(__M_locals))

        def nav():
            return render_nav(context._locals(__M_locals))

        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self)

        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin(
            [(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if
             __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)

        __M_writer('\n\n')
        __M_writer(
            '    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n    <script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/jquery.form.js"></script>\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer(
            'homepage/scripts/jquery.loadmodal.js"></script>\n\n    <!-- Latest compiled and minified CSS -->\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\n    <link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">\n\n    <!-- Latest compiled and minified JavaScript -->\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n    <link rel="shortcut icon" type="image/jpeg" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/favicon.ico">\n\n')
        __M_writer('    ')
        __M_writer(str(static_renderer.get_template_css(request, context)))
        __M_writer(
            '\n  \n  </head>\n  \n  <body>\n  \n    <div id="header" class="container-fluid">\n      <header>\n          <div>\n              Colonial Heritage Foundation\n              <span class="label label-warning">\n                  <span class="glyphicon glyphicon-tower" aria-hidden="true"></span>\n              </span>\n          </div>\n      </header>\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav'):
            context['self'].nav(**pageargs)

        __M_writer(
            '\n    </div>\n  \n    <div id="leftside" class="col-md-2">\n        <div id="buttons" style="text-align: center;">\n            <p style="text-align:center">Which color do you prefer?</p>\n            <button type="button" class="btn btn-primary btn-lg" style="width:75px;">Blue</button>\n            <button type="button" class="btn btn-success btn-lg">Green</button>\n        </div> <!--buttons-->\n        <p style="margin-top:20px; text-align:center;">\n            <button type="button" class="btn btn-info btn-sm">\n                <span class="glyphicon glyphicon-thumbs-up" aria-hidden="true"></span> Like\n            </button>\n        </p>\n    </div> <!--leftside-->\n\n    <div id="center" class="col-md-10">\n        <div id="login_dialog" class="modal fade">\n            <div class="modal-dialog">\n                <div class="modal-content">\n                    <div class="modal-header">\n                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n                        <h4 class="modal-title">Sign In</h4>\n                    </div>\n                    <div class="modal-body">\n                        <p>One fine body&hellip;</p>\n                    </div>\n                </div><!-- /.modal-content -->\n            </div><!-- /.modal-dialog -->\n        </div><!-- /.modal -->\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)

        __M_writer(
            '\n    </div> <!-- center -->\n\n    <div id="footer" class="container-fluid">\n      <footer>\n        <p style="text-align:center;">\n          <span class="glyphicon glyphicon-copyright-mark" aria-hidden="true"></span>\n          Bigfoot\n        </p>\n      </footer>\n    </div>\n  \n')
        __M_writer('    ')
        __M_writer(str(static_renderer.get_template_js(request, context)))
        __M_writer('\n  \n  </body>\n\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)

        __M_writer = context.writer()
        __M_writer('\n        <title>Colonial Heritage Foundation</title>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)

        __M_writer = context.writer()
        __M_writer('\n        Site content goes here in sub-templates.\n      ')
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
            '\n        <div id="outside_nav">\n          <nav class="navbar navbar-inverse">\n              <div id="inside_navbar" class="container-fluid">\n                <ul class="nav navbar-nav">\n                    <li role="presentation" ')
        __M_writer(str('class="active"' if request.dmp_router_page == 'index' else ''))
        __M_writer('>\n                        <a href="/homepage/index">Home</a>\n                    </li>\n')
        if request.user.is_authenticated() and request.user.groups.all()[0].name == 'Administrator':
            __M_writer('                        <li role="presentation" ')
            __M_writer(str('class="active"' if request.dmp_router_page == 'users' else ''))
            __M_writer(
                '>\n                            <a href="/homepage/users">Users</a>\n                        </li>\n')
        if request.user.is_authenticated() and (
                request.user.groups.all()[0].name == 'Manager' or request.user.groups.all()[0].name == 'Administrator'):
            __M_writer('                        <li role="presentation" ')
            __M_writer(str('class="active"' if request.dmp_router_page == 'product' else ''))
            __M_writer(
                '>\n                            <a href="/homepage/product">Products</a>\n                        </li>\n                        <li class="dropdown">\n                            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Owners <span class="caret"></span></a>\n                            <ul class="dropdown-menu" role="menu">\n                                <li ')
            __M_writer(str('class="active"' if request.dmp_router_page == 'person' else ''))
            __M_writer(
                '>\n                                    <a href="/homepage/person/">Individuals</a>\n                                </li>\n                                <li role="presentation" ')
            __M_writer(str('class="active"' if request.dmp_router_page == 'organization' else ''))
            __M_writer(
                '>\n                                    <a href="/homepage/organization/">Organizations</a>\n                                </li>\n                            </ul>\n                        </li>\n                        <li role="presentation" ')
            __M_writer(str('class="active"' if request.dmp_router_page == 'event' else ''))
            __M_writer(
                '>\n                            <a href="/homepage/event">Events</a>\n                        </li>\n                        <li role="presentation" ')
            __M_writer(str('class="active"' if request.dmp_router_page == 'report' else ''))
            __M_writer(
                '>\n                            <a href="/homepage/report">Overdue Items Report</a>\n                        </li>\n')
        __M_writer('                    <li role="presentation" ')
        __M_writer(str('class="active"' if request.dmp_router_page == 'rental_items' else ''))
        __M_writer(
            '>\n                        <a href="/homepage/rental_items">Check In Rental Items</a>\n                    </li>\n                    <li role="presentation" ')
        __M_writer(str('class="active"' if request.dmp_router_page == 'rental_products' else ''))
        __M_writer(
            '>\n                        <a href="/homepage/rental_products">Rental Products</a>\n                    </li>\n                </ul>\n                <ul class="nav navbar-nav navbar-right">\n')
        if request.user.is_authenticated():
            __M_writer('                        <p class="navbar-text">Welcome, ')
            __M_writer(str(request.user.first_name))
            __M_writer(
                '!</p>\n                        <button type="button" id="view_rental_cart" class="btn btn-warning navbar-btn">\n                            View Cart <span class="glyphicon glyphicon-shopping-cart" aria-hidden="true"></span>\n                        </button>\n                        <a href="/homepage/login.logout_view" class="btn btn-warning navbar-btn">Sign Out</a>\n')
        else:
            __M_writer(
                '                        <button id="show_login_dialog_nav" type="button" class="btn btn-warning navbar-btn">Sign In</button>\n')
        __M_writer('                </ul>\n              </div>\n          </nav>\n        </div>\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 89, "129": 89, "130": 89, "131": 94, "132": 95, "133": 97, "139": 133, "16": 4, "18": 0, "32": 2, "33": 4, "34": 5, "38": 5, "43": 13, "44": 16, "45": 18, "46": 18, "47": 19, "48": 19, "49": 27, "50": 27, "51": 30, "52": 30, "53": 30, "58": 101, "63": 133, "64": 146, "65": 146, "66": 146, "72": 11, "78": 11, "84": 131, "90": 131, "96": 45, "103": 45, "104": 50, "105": 50, "106": 53, "107": 54, "108": 54, "109": 54, "110": 58, "111": 59, "112": 59, "113": 59, "114": 65, "115": 65, "116": 68, "117": 68, "118": 73, "119": 73, "120": 76, "121": 76, "122": 80, "123": 80, "124": 80, "125": 83, "126": 83, "127": 88}, "source_encoding": "ascii", "filename": "/Users/Nate/chf_dmp/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm"}
__M_END_METADATA
"""
