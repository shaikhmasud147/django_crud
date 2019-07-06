# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from testapp.models import Employee

# Create your views here.

def model_view(request):
    employees = Employee.objects.all()
    my_dict = {'employees': employees}
    return render(request, 'testapp/result.html', my_dict)
