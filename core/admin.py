from django.contrib import admin
from django.contrib.auth import models

# Register your models here.
from core.models import Company, Department, Employee


class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "legal_number", "created_at"]


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["company", "name", "status", "created_at"]


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "first_name",
        "last_name",
        "company",
        "department",
        "role",
        "joining_date",
        "salary",
        "created_at",
    ]


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Company, CompanyAdmin)
