from django.contrib import admin

from .models import Employee
from .utility.export_data import export_to_csv

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'emp_name',
        'emp_email',
        'emp_id',
        'emp_phone',
        'department',
        'join_date',
        'profile',
        'cf',
        'status'
    )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        queryset = self.model.objects.all()
        fields = [
            'emp_name',
            'emp_email',
            'emp_id',
            'emp_phone',
            'department',
            'join_date',
            'profile',
            'cf',
            'status'
        ]  # Same fields as in list_display
        filename = 'your_model_data.csv'
        export_to_csv(queryset, fields, filename)
