from django.db import models
from month.models import MonthField
from datetime import date


# Create your models here.

class Employee(models.Model):
    DEPT_CHOICES = [
        ('PYTHON', 'PYTHON'),
        ('JAVA', 'JAVA'),
        ('EMBEDDED SYSTEMS', 'EMBEDDED SYSTEMS'),
        ('MATLAB', 'MATLAB'),
        ('VLSI', 'VLSI')
    ]
    emp_name = models.CharField(max_length=255)
    emp_email = models.EmailField(unique=True)
    emp_id = models.CharField(max_length=10, unique=True)
    emp_phone = models.CharField(max_length=15, unique=True)
    emp_alt_phone = models.CharField(max_length=15, null=True, blank=True)
    department = models.CharField(choices=DEPT_CHOICES, max_length=25)
    join_date = models.DateField(default=date.today)
    profile = models.ImageField(upload_to='static/profiles')
    cf = models.PositiveIntegerField(default=0)
    address = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.emp_id

class AttendanceForm(models.Model):
    monthly_form = MonthField()
    date_created = models.DateTimeField(auto_now_add=True)
    month_form = str(monthly_form)

    def __str__(self):
        return self.month_form

    
