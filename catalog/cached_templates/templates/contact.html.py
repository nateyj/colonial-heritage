# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422408391.994026
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/contact.html'
_template_uri = 'contact.html'
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
            '\n\t<p>\n  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque id purus et mauris ullamcorper facilisis. Nunc lobortis pulvinar velit, ut fermentum quam fringilla quis. Etiam velit orci, molestie at metus ut, commodo iaculis neque. Ut quis posuere sem. Maecenas imperdiet tincidunt justo, vitae efficitur nunc molestie tempor. Nulla vel leo dui. Nam non erat vel libero imperdiet congue quis sit amet sapien.\n  </p>\n  <p>\n  Ut a vehicula dui. Ut ullamcorper vitae lorem fermentum accumsan. Proin vel interdum velit, ac mollis turpis. Maecenas nisi nibh, dignissim a nulla at, scelerisque ullamcorper ante. Aenean laoreet arcu non tincidunt ultrices. Aenean id nisl rhoncus, lobortis nisl et, rhoncus sem. In porttitor, justo ac rhoncus vulputate, velit mauris iaculis mauris, nec placerat mauris ante quis risus. Quisque porta nisi in posuere dictum. Quisque pellentesque malesuada leo, non interdum tellus vehicula et. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Praesent orci velit, iaculis eget massa eget, porttitor tincidunt justo. Duis viverra ex quam, id gravida enim venenatis vitae. Duis nec libero congue, tempus dolor eget, mollis ante. Vivamus ac urna sit amet quam lacinia condimentum. Curabitur ante odio, lobortis vitae odio sed, mattis consectetur quam. Integer commodo scelerisque quam, eu fringilla ex tristique ac.\n  </p>\n  <p>\n  In leo risus, scelerisque id sapien et, rhoncus sagittis eros. Curabitur malesuada erat a purus ullamcorper suscipit. Praesent elementum, ante in posuere porttitor, lectus nunc maximus orci, et venenatis eros ligula in orci. Donec vitae sodales sem. Proin nec lacus iaculis, sagittis velit a, volutpat nisi. Duis blandit condimentum tellus, quis ornare ante egestas at. Nullam fringilla nisi a lorem finibus, vel lobortis nisl mollis. Quisque at iaculis diam, vitae tempor massa. Proin sodales diam at lectus laoreet, sit amet tincidunt lacus aliquet. Aenean cursus ullamcorper nisi, eget bibendum enim ultricies sit amet. Cras sed erat id sapien gravida fringilla. Vivamus consectetur nisi nibh, et bibendum quam interdum at. Aliquam consectetur tellus sem, a commodo orci accumsan nec. Aliquam erat volutpat. Fusce a placerat lectus.\n  </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "uri": "contact.html", "filename": "/Users/Nate/chf_dmp/homepage/templates/contact.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
