from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework import viewsets

from .forms import CompanyForm, DepartmentForm, EmployeeForm
from .models import Company, Department, Employee
from .serializer import (
    CompanySerializer,
    DepartmentSerializer,
    EmployeeSerializer,
)


def index(request):
    companies = Company.objects.all()
    return render(request, "core/companies.html", {"companies": companies})


def company(request, pk):
    company = Company.objects.get(id=pk)
    return render(request, "core/company.html", {"company": company})


def createCompany(request):
    form = CompanyForm()

    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "core/company-form.html", {"form": form})


def editCompany(request, pk):
    page = "edit"
    company = Company.objects.get(id=pk)
    form = CompanyForm(instance=company)

    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect("company", pk=company.id)
    return render(
        request, "core/company-form.html", {"form": form, "page": page}
    )


def deleteCompany(request, pk):
    company = Company.objects.get(id=pk)
    if request.method == "POST":
        company.delete()
        return redirect("index")
    return render(request, "core/delete-company.html", {"company": company})


def employees(request, pk):
    company = Company.objects.get(id=pk)
    return render(request, "core/employees.html", {"company": company})


def createEmployee(request, pk):
    company = Company.objects.get(id=pk)
    if request.method == "POST":
        print(request.POST)
        form = EmployeeForm(request.POST)
        if form.is_valid():
            new_employee = form.save(commit=False)
            new_employee.company = company
            new_employee.save()
            return redirect("employees", pk=company.id)
        else:
            print(form.errors)
            return render(
                request,
                "core/employee-form.html",
                {"company": company, "form": form},
            )
    return render(request, "core/employee-form.html", {"company": company})


def editEmployee(request, pk):
    page = "edit"
    employee = Employee.objects.get(id=pk)
    company = Company.objects.get(id=employee.company.id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            edit_employee = form.save(commit=False)
            edit_employee.company = company
            edit_employee.save()
            return render(request, "core/employees.html", {"company": company})
        else:
            return render(
                request,
                "core/employee-form.html",
                {
                    "company": company,
                    "employee": employee,
                    "page": page,
                    "form": form,
                },
            )
    return render(
        request,
        "core/employee-form.html",
        {"company": company, "employee": employee, "page": page},
    )


def deleteEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return redirect("employees", pk=employee.company.id)


def departments(request, pk):
    company = Company.objects.get(id=pk)
    return render(request, "core/departments.html", {"company": company})


def createDepartments(request, pk):
    form = DepartmentForm()
    company = Company.objects.get(id=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        dp = form.save(commit=False)
        dp.company = company
        if not dp.status:
            dp.status = False
        dp.save()
        return redirect("departments", pk=company.id)
    return render(
        request,
        "core/department-form.html",
        {"form": form, "company": company},
    )


def editDepartment(request, pk):
    page = "edit"
    department = Department.objects.get(id=pk)
    form = DepartmentForm(instance=department)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid:
            form.save()
            return redirect("departments", pk=department.company.id)
    return render(
        request, "core/department-form.html", {"page": page, "form": form}
    )


def deleteDepartment(request, pk):
    dp = Department.objects.get(id=pk)
    department = Department.objects.get(id=pk)
    try:
        department.delete()
    except:
        return redirect("departments", pk=dp.company.id)
    return redirect("departments", pk=dp.company.id)


##### APIs #####


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
