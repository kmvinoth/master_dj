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

from django.conf.urls import url, include  # url and include are functions
from django.contrib import admin  # admin is the package
# Loading the views from auth and the template from Registration-defaults
from django.contrib.auth.views import login, logout
from books.views import *

urlpatterns = [
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
    url(r'^digis/admin/', admin.site.urls),
    url(r'^login/$', login, {'template_name': 'login.html', 'extra_context': {'next': '/login_success'}}),
    url(r'^login_success/$', project_member_view),
    url(r'^logout/$', logout, {'template_name': 'logout.html', 'extra_context': {'next': '/signout'}}),
    url(r'^hello/$', hello),
    url(r'^datetime/$', current_datetime),
    url(r'time/plus/(\d{1,2})/$', hours_ahead)
]
