"""master_dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# r'^$' empty string (url) used for the homepage (defined in the view)

from django.conf.urls import url
# Admin views
from django.contrib import admin
# Authentication views that are built in django
from django.contrib.auth.views import login, logout
# Views from the local module
from books.views import*

urlpatterns = [
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
    url(r'^digis/admin/', admin.site.urls),
    url(r'^login/$', std_login),
    url(r'^login/accounts/std_auth$', std_auth),
    url(r'^ldap_login/$', ldap_login),
    url(r'^ldap_login/accounts/ldap_auth$', ldap_auth),
    # url(r'^login/$', login, {'template_name': 'login.html', 'extra_context': {'next': '/login_success'}}),
    url(r'^login_success/$', project_member_view),
    url(r'^metadata/$', metadata),
    url(r'^loggedout/$', logout, {'template_name': 'logout.html', 'extra_context': {'next': '/logout'}}),
]
