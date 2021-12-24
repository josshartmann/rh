from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets

from core import models

from .models import Company, Department, Employee


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {"class": "custom-input", "autocomplete": "off"}
        )

        self.fields["legal_number"].widget.attrs.update(
            {"class": "custom-input", "autocomplete": "off"}
        )


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        exclude = ["company "]
        fields = ["name", "status"]

        widgets = {
            "status": forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {"class": "custom-input", "autocomplete": "off"}
        )
        self.fields["status"].widget.attrs.update(
            {"class": "form-check-input"}
        )


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = ()
        fields = [
            "first_name",
            "last_name",
            "age",
            "user",
            "joining_date",
            "email",
            "phone",
            "gender",
            "department",
            "role",
            "salary",
        ]
