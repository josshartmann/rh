from core import views
from django.test import SimpleTestCase
from django.urls import resolve, reverse


class TestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse("index")
        self.assertEquals(resolve(url).func, views.index)

    def test_company_url(self):
        url = reverse("company", args=["pk"])
        self.assertEquals(resolve(url).func, views.company)

    def test_create_company_url(self):
        url = reverse("create-company")
        self.assertEquals(resolve(url).func, views.createCompany)

    def test_edit_company_url(self):
        url = reverse("edit-company", args=["pk"])
        self.assertEquals(resolve(url).func, views.editCompany)

    def test_delete_company_url(self):
        url = reverse("delete-company", args=["pk"])
        self.assertEquals(resolve(url).func, views.deleteCompany)

    def test_employee_url(self):
        url = reverse("employees", args=["pk"])
        self.assertEquals(resolve(url).func, views.employees)

    def test_create_employee_url(self):
        url = reverse("create-employee", args=["pk"])
        self.assertEquals(resolve(url).func, views.createEmployee)

    def test_edit_employee_url(self):
        url = reverse("edit-employee", args=["pk"])
        self.assertEquals(resolve(url).func, views.editEmployee)

    def test_delete_employee_url(self):
        url = reverse("delete-employee", args=["pk"])
        self.assertEquals(resolve(url).func, views.deleteEmployee)

    def test_departments_url(self):
        url = reverse("departments", args=["pk"])
        self.assertEquals(resolve(url).func, views.departments)

    def test_create_department_url(self):
        url = reverse("create-department", args=["pk"])
        self.assertEquals(resolve(url).func, views.createDepartments)

    def test_edit_department_url(self):
        url = reverse("edit-department", args=["pk"])
        self.assertEquals(resolve(url).func, views.editDepartment)

    def test_delete_department_url(self):
        url = reverse("delete-department", args=["pk"])
        self.assertEquals(resolve(url).func, views.deleteDepartment)
