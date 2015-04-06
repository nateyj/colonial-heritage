# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423363760.502459
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/organization.html'
_template_uri = 'organization.html'
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
        organizations = context.get('organizations', UNDEFINED)

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
        organizations = context.get('organizations', UNDEFINED)

        def content():
            return render_content(context)

        __M_writer = context.writer()
        __M_writer(
            '\n\n<div class="text-left">\n    <h1 class="page-header">Organizations</h1>\n</div>\n\n<div class="text-left" style="margin-bottom: 20px;">\n    <a href="/homepage/organization.create/" class="btn btn-warning">Add New Organization</a>\n</div>\n\n<table id="organization_table" class="table table-striped">\n    <tr>\n        <th>Actions</th>\n        <th>ID</th>\n        <th>Name</th>\n        <th>Address</th>\n        <th>City</th>\n        <th>State</th>\n        <th>ZIP</th>\n        <th>Country</th>\n        <th>Email</th>\n    </tr>\n')
        for organization in organizations:
            __M_writer('        <tr>\n            <td>\n                <a href="/homepage/organization.edit/')
            __M_writer(str(organization.id))
            __M_writer('/">Edit</a>\n                |\n                <a href="/homepage/organization.delete/')
            __M_writer(str(organization.id))
            __M_writer('/">Delete</a>\n            </td>\n            <td>')
            __M_writer(str(organization.id))
            __M_writer('</td>\n            <td>')
            __M_writer(str(organization.given_name))
            __M_writer('</td>\n            <td>')
            __M_writer(str(organization.address1))
            __M_writer('</td>\n            <td>')
            __M_writer(str(organization.city))
            __M_writer('</td>\n            <td>')
            __M_writer(str(organization.state))
            __M_writer('</td>\n            <td>')
            __M_writer(str(organization.zip))
            __M_writer('</td>\n            <td>')
            __M_writer(str(organization.country))
            __M_writer('</td>\n            <td>')
            __M_writer(str(organization.email))
            __M_writer('</td>\n        </tr>\n')
        __M_writer('</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "organization.html", "filename": "/Users/Nate/chf_dmp/homepage/templates/organization.html", "line_map": {"64": 34, "65": 35, "66": 35, "67": 36, "68": 36, "69": 37, "70": 37, "71": 38, "72": 38, "73": 39, "74": 39, "75": 42, "81": 75, "27": 0, "35": 1, "45": 3, "52": 3, "53": 25, "54": 26, "55": 28, "56": 28, "57": 30, "58": 30, "59": 32, "60": 32, "61": 33, "62": 33, "63": 34}, "source_encoding": "ascii"}
__M_END_METADATA
"""
