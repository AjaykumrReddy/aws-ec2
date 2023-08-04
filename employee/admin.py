from django.contrib import admin
from .models import EmployeeLeaves
# Register your models here.


class EmployeeLeavesAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'emp_id',
        'emp_name',
        'earned_leave',
        'casual_leave',
        'sick_leave',
        'maternity_leave',
        'leave_reason',
        'leavefrom',
        'leaveto',
        'leave_days',
    )


admin.site.register(EmployeeLeaves, EmployeeLeavesAdmin)
