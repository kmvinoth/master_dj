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

from books.views import hello, home, current_date_time, hours_ahead

urlpatterns = [
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^datetime/$', current_date_time),
    url(r'time/plus/(\d{1,2})/$', hours_ahead)
]
