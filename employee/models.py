from django.db import models

# Create your models here.


class EmployeeLeaves(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    emp_id = models.CharField(max_length=10)
    emp_name = models.CharField(max_length=255)
    earned_leave = models.BooleanField(default=False)
    casual_leave = models.BooleanField(default=False)
    sick_leave = models.BooleanField(default=False)
    maternity_leave = models.BooleanField(default=False)
    leave_reason = models.TextField()
    leavefrom = models.DateField()
    leaveto = models.DateField()
    leave_days = models.PositiveIntegerField()

    def __str__(self):
        return self.emp_id

