# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def date_time(request):
    date = datetime.datetime.now()
    html = '<h2> Current system time is' + str(date) + '<h2>'
    return HttpResponse(html)