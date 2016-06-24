from django.http import HttpResponse, HttpResponseRedirect  # HttpResponse is a class
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django_python3_ldap import ldap
from .forms import LoginForm
from .models import *


def home(request):
    return render(request, 'home.html')


# View for Standard login template
def std_login(request):

    print(request.META)

    form = LoginForm
    context = {'form': form}
    return render(request, 'login.html', context)


# View for Standard authentication and login
def std_auth(request):

    print(request.META)
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        user = authenticate(username=username, password=password)
        if user.backend == 'django.contrib.auth.backends.ModelBackend':
            login(request, user)
            return HttpResponseRedirect('/login_success')
        else:
            return HttpResponse("Select the appropriate login like LDAP or Oauth")

    except AttributeError:
        print("Authentication fails and returns None object")
        return HttpResponse("User not in the database")


# View for LDAP login template
def ldap_login(request):
    return render(request, 'ldap_login.html')


def ldap_auth(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # ldap authenticate
    user = ldap.authenticate(username=username, password=password)
    # ldap authenticate does not set an backend attribute on the user object
    # (which is required for the login function), so you have set that manually
    user.backend = 'django_python3_ldap.auth.LDAPBackend'
    user.save()

    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/login_success')
    else:
        return HttpResponse('Invalid(LDAP) username or password credentials')


# After authentication and login this view decides who gets what
def project_member_view(request):
    if request.user.groups.filter(name='Project_admin').exists():
        return project_admin_view(request)
    else:
        return render(request, 'Project_member.html')


def project_admin_view(request):
    return render(request, 'Project_admin.html')