# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello_message(request):
    html = '<h2> Hello, Django First App <h2>'
    return HttpResponse(html)
