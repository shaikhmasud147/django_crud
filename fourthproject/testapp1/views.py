# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import datetime
# Create your views here.

def template_views(request):
    dt = datetime.datetime.now()
    name = "Masud Shaikh"
    add = "Pune"
    mob_no = 9028853096
    my_dict = {'date' : dt, 'name' : name, 'address' : add, 'mobile_no': mob_no}
    return render(request,'testapp1/results.html', my_dict)
