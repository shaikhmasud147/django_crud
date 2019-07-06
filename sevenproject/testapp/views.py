# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def django_view(request):
    return render(request, 'testapp/index.html')

def movie_news(request):
    news1 = 'Amir Khan loss movie in this year'
    news2 = 'Sharukh and Salman now friends'
    news3 = 'Shra Ali Khan made good acting in Shimbha movie'

    my_dict = {'n1': news1, 'n2': news2, 'n3': news3}
    return render(request, 'testapp/movie_news.html', my_dict)