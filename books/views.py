from django.http import HttpResponse, HttpResponseRedirect  # HttpResponse is a class
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django_python3_ldap import ldap
from .models import *
import rules
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    return render(request, 'home.html')


# View for Standard login template
def std_login(request):
    return render(request, 'login.html')


# View for Standard authentication and login
def std_auth(request):
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
        return HttpResponse("Invalid username or password")


# View for LDAP login template
def ldap_login(request):
    return render(request, 'ldap_login.html')


def ldap_auth(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        # ldap authenticate
        user = ldap.authenticate(username=username, password=password)
        # ldap authenticate does not set an backend attribute on the user object
        # (which is required for the login function), so you have set that manually
        user.backend = 'django_python3_ldap.auth.LDAPBackend'
        user.save()

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/login_success')

    except AttributeError:
        print("Authentication fails and returns None object")
        return HttpResponse('Invalid(LDAP) username or password')


# After authentication and login this view decides who gets what

def project_member_view(request):

    # If the user is added as Project admin, he get's the Admin (project admin) link in his page,
    # so that he can do admin activities for the specified project
    # else the user gets the project member view
    try:
        mem_inst = ProjectMember.objects.get(user=request.user)
        # cast mem_inst.role to string
        role     = str(mem_inst.role)
        project  = str(mem_inst.project)
        # print(role)
        if role == 'Admin':
            return render(request, 'Project_admin.html', {'projects': project})
        else:
            return render(request, 'Project_member.html', {'projects': project})
    except ObjectDoesNotExist:
        return HttpResponse('The user has not been assigned to any Project')


def project_admin_view(request):
    return render(request, 'Project_admin.html')


# View to display the projects in which the user is a project member (irrespective of the role)
def display_projects_to_member(request):
        pr_inst = ProjectMember.objects.get(user=request.user)
        project = str(pr_inst.project)
        return render(request, 'projects.html', {'projects': project})


# View to display the project content to the project member
def display_project_content(request):
    return HttpResponse("Your project content will displayed soon to you")


# Views related to Project admin
def admin_edit_project(request):
    pr_inst = ProjectMember.objects.get(user=request.user)
    project = str(pr_inst.project)
    return render(request, 'modify_project.html', {'projects': project})


# Views related to Project admin
def add_user_to_project(request):
    add_user_form = ProjectMemberForm
    form_inst = ProjectMemberForm(request.POST)
    form_inst.save()
    return render(request, 'Add_user_to_project_form.html', {'form': add_user_form})


# Views related to Project admin
def add_metadata_to_project(request):
        return HttpResponse("Display project_metadata.html form")
