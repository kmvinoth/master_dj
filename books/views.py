import _datetime  # built in date time

from django.http import Http404, HttpResponse    # HttpResponse is a class


# Create your views here.
# Function based views
# Homepage


def home(request):
    return HttpResponse("Homepage")

# First view (static)


def hello(request):
    return HttpResponse("Django Powered Page")

# Second view (dynamic content but URL Static)


def current_date_time(request):
    now = _datetime.datetime.now()
    html = "<html><body> It is now %s.</body></html>" % now
    return HttpResponse(html)

# Third View (Dynamic URL's with dynamic content)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = _datetime.datetime.now() + _datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

