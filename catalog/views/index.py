from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import random
from django.utils import timezone

templater = get_renderer('catalog')


@view_function
def process_request(request):
    params = {
        'now': datetime.now().strftime(request.urlparams[0] or '%b %d, %Y %I:%M %p'),
        'timecolor': random.choice(['red', 'blue', 'green', 'brown'])
    }

    return templater.render_to_response(request, 'index.html', params)


@view_function
def get_time(request):
    template_vars = {
        'now': datetime.now(),
        'timecolor': random.choice(['red', 'blue', 'green', 'brown'])
    }

    return templater.render_to_response(request, 'index_time.html', template_vars)