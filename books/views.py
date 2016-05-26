import _datetime  # built in date time

from django.http import Http404, HttpResponse  # HttpResponse is a class
from django.shortcuts import render
from django.contrib.auth.models import User
from django_python3_ldap.ldap import authenticate

# Create your views here.
# Function based views
# Homepage


def home(request):
    return render(request, 'home.html')


def ldap_auth(request):

    return render(request, "ldap_login.html")


def ldap_sucess(request):
    uname = request.POST.get('username')
    pwd   = request.POST.get('password')

    user = authenticate(username=uname, password=pwd)

    if user is not None:
        return HttpResponse("User is authenticated using LDAP credentials")
    else:
        return HttpResponse("User is None")


# After authentication and login this view decides who gets what
def project_member_view(request):
    if request.user.groups.filter(name='Project_admin').exists():
        return project_admin_view(request)
    else:
        return render(request, 'Project_member.html')


def project_admin_view(request):
    return render(request, 'Project_admin.html')


# project changes
def admin_view(request):

    if request.user.groups.filter(name='Project_admin').exists():
        return HttpResponse("Show only the Digis admin content")


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
