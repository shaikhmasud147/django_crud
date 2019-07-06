# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
    rollno = models.IntegerField()
    sname = models.CharField(max_length = 64)
    marks = models.IntegerField()
    mob_no = models.CharField(max_length = 64)
    address = models.TextField()

    def __str__(self):
        return super(Student, self).__str__()


