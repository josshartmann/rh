import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Company(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )

    name = models.CharField(max_length=100, null=True)
    legal_number = models.CharField(max_length=100, null=True)
    logo = models.ImageField(null=True, default="default.jpg")

    # This is auto created and updated date
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_at"]


class Department(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False, null=True)
    admin = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # This is auto created and updated date
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)

    def __str__(self):
        return str(self.name)


class Employee(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, null=True, blank=True)
    GENDER = (("M", "Male"), ("F", "Female"), ("O", "Others"))
    gender = models.CharField(max_length=1, choices=GENDER)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True
    )
    phone = models.CharField(max_length=14, null=True, blank=True)
    role = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    joining_date = models.DateField(null=True)
    salary = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    # This is auto created and updated date
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)

    # Simple title return queue for django admin or auto template
    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ["joining_date"]
