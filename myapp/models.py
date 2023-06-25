from django.db import models

# Create your models here.


class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science'),
        ('ME', 'Mechanical Engineering'),
        ('EE', 'Electrical Engineering'),
        ('CE', 'Civil Engineering'),
    ]

    name = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return f"{self.name} belongs to the department {self.department}"
