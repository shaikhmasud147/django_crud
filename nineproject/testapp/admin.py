# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from testapp.models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    student_list = ['rollno', 'sname', 'marks']

admin.site.register(Student, StudentAdmin)

