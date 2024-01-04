from django.shortcuts import render, redirect, get_object_or_404
from django.http import  HttpResponse
from .models import Employee

# Create your views here.


def home(request):
    employees = Employee.objects.all()
    return render(request, "home.html", {'employees': employees})


def add_emp(request):
    if request.method == "POST":
        emp_data = {
            'name': request.POST.get("emp_name"),
            'employee_id': request.POST.get("emp_id"),
            'phone': request.POST.get("emp_phone"),
            'address': request.POST.get("emp_address"),
            'working': bool(request.POST.get("emp_working")),
            'department': request.POST.get("emp_department"),
        }
        Employee.objects.create(**emp_data)
        return redirect("home")

    return render(request, "add_emp.html", {})


def update_emp(request, emp_id):
    emp = get_object_or_404(Employee, employee_id=emp_id)

    if request.method == 'POST':
        emp.name = request.POST.get("emp_name")
        emp.phone = request.POST.get("emp_phone")
        emp.address = request.POST.get("emp_address")
        emp.employee_id = request.POST.get("emp_id")
        emp.department = request.POST.get("emp_department")
        emp.working = bool(request.POST.get("emp_working"))
        emp.save()
        return redirect("home")

    return render(request, "update_emp.html", {'emp': emp})


def delete_emp(request, emp_id):
    emp = get_object_or_404(Employee, pk=emp_id)
    emp.delete()
    return redirect("home")