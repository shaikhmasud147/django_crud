# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pdb
from django.shortcuts import render, redirect
from employees.forms import EmployeeForm
from employees.models import Employee

# Create your views here.

def add(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/employees/')
            except:
                pass
    else:
        form = EmployeeForm()
        my_dict = {'form' : form}
        return render(request, 'employees/index.html', my_dict)

def employee_view(request):
    employee_list = Employee.objects.all()
    my_dict = {'employees' : employee_list}
    return render(request, 'employees/view.html', my_dict)

def employee_edit(request, id):
    employee = Employee.objects.get(id = id)
    my_dict = {'employee': employee}
    return render(request, 'employees/edit.html', my_dict)

def employee_update(request, user_id):
    # pdb.set_trace()
    employee = Employee.objects.get(id = user_id)  
    my_dict = {'employee': employee}
    # form = EmployeeForm(request.POST, instance = employee)  
    if request.method == "POST":
        form = EmployeeForm(request.POST or None, instance = employee)
        # for key in request.POST:
        #     print(key)
        #     value = request.POST["ename"]
        #     print(value)
        
        if form.is_valid():  
            try:
                form.save()
                return redirect('/employees/')
            except:
                raise("Form is not valid")
        else:
            return render(request, 'employees/edit.html', my_dict)      
    else:
        return render(request, 'employees/edit.html', my_dict)  

def employee_delete(request, id):
    employee = Employee.objects.get(id = id)
    employee.delete()
    return redirect('/employees/')