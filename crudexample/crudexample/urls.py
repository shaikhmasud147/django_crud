"""crudexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from employees import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^employees/', include('employees.urls')),
    # url(r'^add', views.add),
    # url(r'^view', views.employee_view),
    # url(r'^edit/(\d+)/$', views.employee_edit),
    # url(r'^update/(\d+)/$', views.employee_update),
    # url(r'^delete/(\d+)/$', views.employee_delete),
]
