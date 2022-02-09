
from django.shortcuts import render
from crud.models import Employee_info
from crud import forms

# Create your views here.

def index(request):
    info=Employee_info.objects.order_by('name')
    dic={'retrive_data':info}
    return render(request,'index.html',context=dic)

def addEmployee(request):
    add_form=forms.EmployeeForm()
    dic={}
    if request.method=='POST':
        add_form=forms.EmployeeForm(request.POST)
        if add_form.is_valid():
            add_form.save(commit=True)
            return index(request)

    dic.update({'addandupdate':"Add Employee",'form':add_form})
    return render(request,'addEmployee.html',context=dic)

def edit(request,id):
    employee_info=Employee_info.objects.get(pk=id)
    edit_employee=forms.EmployeeForm(instance=employee_info)
    dic={}
    if request.method=='POST':
        edit_employee=forms.EmployeeForm(request.POST,instance=employee_info)
        if edit_employee.is_valid():
            edit_employee.save(commit=True)
            return index(request)
    dic.update({'addandupdate':"Update Employee",'form':edit_employee})

    return render(request,'addEmployee.html',context=dic)

def delete(request,id):
    delete_employee=Employee_info.objects.get(pk=id).delete()
    return index(request)
    


    
