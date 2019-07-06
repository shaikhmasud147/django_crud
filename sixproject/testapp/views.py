# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import datetime

# Create your views here.

def date_time_view(request):
    dt = datetime.datetime.now()
    hr = int(dt.hour)

    if hr<12:
        msg = 'Hello friends Good Morning!!!'
    elif hr<16:
        msg = 'Hello friends Good Afternoon!!!'
    elif hr<20:
        msg = 'Hello friends Good Evening!!!'
    else:
        msg = 'Hello friends Good Night!!!'

    my_dict = {'date': dt, 'msg': msg}
    return render(request, 'testapp/results.html', my_dict) 

