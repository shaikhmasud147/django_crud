# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from testapp.models import Student
# Create your views here.

def student_info(request):
    # studentinfo = Student.objects.all()
    studentinfo = Student.objects.filter(marks__lt = 35)
    # studentinfo = Student.objects.order_by('marks')
    my_dict = {'students':studentinfo}
    return render(request, 'testapp/studentinfo.html', my_dict)

