from django.urls import path
from django.urls.conf import include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"company", views.CompanyViewSet)
router.register(r"department", views.DepartmentViewSet)
router.register(r"employees", views.EmployeeViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    ##### Company Path #####
    path("company/<str:pk>/", views.company, name="company"),
    path("create-company/", views.createCompany, name="create-company"),
    path("edit-company/<str:pk>", views.editCompany, name="edit-company"),
    path(
        "delete-company/<str:pk>/", views.deleteCompany, name="delete-company"
    ),
    ##### Employee Path #####
    path("employees/<str:pk>", views.employees, name="employees"),
    path(
        "create-employee/<str:pk>",
        views.createEmployee,
        name="create-employee",
    ),
    path("edit-employee/<str:pk>", views.editEmployee, name="edit-employee"),
    path(
        "delete-employee/<str:pk>/",
        views.deleteEmployee,
        name="delete-employee",
    ),
    ##### Department Path #####
    path("departments/<str:pk>/", views.departments, name="departments"),
    path(
        "create-department/<str:pk>/",
        views.createDepartments,
        name="create-department",
    ),
    path(
        "edit-department/<str:pk>",
        views.editDepartment,
        name="edit-department",
    ),
    path(
        "delete-department/<str:pk>/",
        views.deleteDepartment,
        name="delete-department",
    ),
    ##### API #####
    path("api/", include(router.urls)),
]
