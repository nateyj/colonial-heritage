# -*- coding:ascii -*-
from mako import runtime, filters, cache

UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426187617.572132
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/catalog/templates/charge_card.html'
_template_uri = 'charge_card.html'
_source_encoding = 'ascii'
import os, os.path, re

_exports = []


def render_body(context, **pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(
            '<!doctype html>\n<html>\n    <head>\n        <title>REST API Example</title>\n        <script src="http:///ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>\n        <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\n        <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">\n        <script src="http:///netdna.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\n    </head>\n    <body style="padding: 2em;">\n        <h1>REST API Example</h1>\n        <pre>\n            Endpoint: http://dithers.cs.byu.edu/iscore/api/v1/charges\n            Valid credit card: Visa, 4732817300654, Exp. 10/15, CVC 411, Cardholder Name: Cosmo Limesandal\n            Sample Charge Creation:\n            curl http://dithers.cs.byu.edu/iscore/api/v1/charges ')
        __M_writer('            -d apiKey=YOUR_API_KEY ')
        __M_writer('            -d currency=usd ')
        __M_writer('            -d amount=5.99 ')
        __M_writer('            -d type=Visa ')
        __M_writer('            -d number=4732817300654 ')
        __M_writer('            -d exp_month=10 ')
        __M_writer('            -d exp_year=15 ')
        __M_writer('            -d cvc=411 ')
        __M_writer('            -d "name=Cosmo Limesandal" ')
        __M_writer(
            '            -d "description=Charge for cosmo@is411.byu.edu"\n            Query Charges:\n            curl --get http://dithers.cs.byu.edu/iscore/api/v1/charges ')
        __M_writer(
            '            -d apiKey=YOUR_API_KEY\n        </pre>\n        <button type="button" class="btn btn-primary" id="charge">Charge</button>\n        <button type="button" class="btn btn-success" id="queryCharges">Query Charges</button>\n        <input type="text" id="chargeId">\n        <br />\n        <div id="message"></div>\n        <script type="text/javascript">\n            $(function() {\n                console.log(\'hello\');\n                $(\'#charge\').click(function() {\n                    console.log(\'Click charge.\');\n                });\n\n                $(\'#queryCharges\').on("click", function() {\n                    console.log(\'queryCharges\');\n                });\n            });\n        </script>\n    </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "charge_card.html", "source_encoding": "ascii", "line_map": {"32": 29, "38": 32, "16": 0, "21": 1, "22": 17, "23": 18, "24": 19, "25": 20, "26": 21, "27": 22, "28": 23, "29": 24, "30": 25, "31": 26}, "filename": "/Users/Nate/chf_dmp/catalog/templates/charge_card.html"}
__M_END_METADATA
"""
