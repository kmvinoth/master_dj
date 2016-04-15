import _datetime  # built in date time

from django.http import Http404, HttpResponse    # HttpResponse is a class
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required


# Create your views here.
# Function based views
# Homepage

def login_success(request):
    return HttpResponse("Your credentials are authenticated, your workspace will be created soon")


def logout_view(request):
    return render(request, 'logout.html')


def home(request):
    return render(request, 'home.html')

# First view (static)


def hello(request):
    return HttpResponse("Django Powered Page")

# Second view (dynamic content but URL Static)


def current_date_time(request):
    now = _datetime.datetime.now()
    html = "<html><body> It is now %s.</body></html>" % now
    return HttpResponse(html)


def current_datetime(request):
    now = _datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

# Third View (Dynamic URL's with dynamic content)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = _datetime.datetime.now() + _datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

