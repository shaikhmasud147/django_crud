# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def good_morning_message(request):
    html = '<h2>Hello friends Good Mornning</h2>'
    return HttpResponse(html)

def good_Afternoon_message(request):
    html = '<h2>Hello friends Good Afternoon</h2>'
    return HttpResponse(html)

def good_evening_message(request):
    html = '<h2>Hello friends Good Evening</h2>'
    return HttpResponse(html)

def good_night_message(request):
    html = '<h2>Hello friends Good Night</h2>'
    return HttpResponse(html)
