# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee(models.Model):
    eno = models.CharField(max_length = 264)
    ename = models.CharField(max_length = 264)
    eemail = models.EmailField()
    contact = models.CharField(max_length = 264)
    address = models.TextField()

    class Meta:
        db_table = 'employee'