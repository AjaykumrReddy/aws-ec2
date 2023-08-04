from django.shortcuts import render
from employee.models import EmployeeLeaves

# Create your views here.


def DatapointAdmin(request):
    return render(request, 'administraion/datapoint_admin.html')


def AdminLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email == 'hr@datapoint.com' and password == 'hr@datapoint.com':
            leave_requests = EmployeeLeaves.objects.all()
            print(leave_requests)
            return render(request, 'administraion/leaverequests.html', {'leave_requests': leave_requests})
        else:
            return render(request, 'administraion/datapoint_admin.html', {'invalid': 'invalid'})
    else:
        return render(request, 'administraion/datapoint_admin.html')

