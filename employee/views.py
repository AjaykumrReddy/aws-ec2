from django.shortcuts import render
from administration.models import Employee

# Create your views here.


def index(request):
    if request.method == "POST":
        emp_email = request.POST.get('emp_email')
        emp_id = request.POST.get('emp_id')
        try:
            employee = Employee.objects.get(emp_email=emp_email, emp_id=emp_id)
            if employee.status == True:
                request.session['emp_id'] = emp_id
                return render(request, 'employee_overview.html', {'employee': employee})
            else:
                return render(request, 'index.html', {'blocked': 'blocked'})
        except Exception as e:
            return render(request, 'index.html', {'exception': e})

    else:
        return render(request, 'index.html')


def employee_overview(request):
    try:
        emp_id = request.session['emp_id']
        employee = Employee.objects.get(emp_id=emp_id)
        if employee.status == True:
            request.session['emp_id'] = emp_id
            return render(request, 'employee_overview.html', {'employee': employee})
        else:
            return render(request, 'index.html', {'blocked': 'blocked'})
    except Exception as e:
        return render(request, 'index.html')


def employee_portfolio(request):
    try:
        emp_id = request.session['emp_id']
        employee = Employee.objects.get(emp_id=emp_id)
        if employee.status == True:
            request.session['emp_id'] = emp_id
            return render(request, 'employee_portfolio.html', {'employee': employee})
        else:
            return render(request, 'index.html', {'blocked': 'blocked'})
    except Exception as e:
        return render(request, 'index.html')


def leave_application(request):
    emp_id = request.session['emp_id']
    employee = Employee.objects.get(emp_id=emp_id)
    return render(request, 'leave_application.html', {'employee': employee})


def leaveform_submit(request):
    import datetime
    emp_id = request.session['emp_id']
    employee = Employee.objects.get(emp_id=emp_id)
    if request.method == 'POST':
        earned_leave = request.POST.get('earned_leave')
        casual_leave = request.POST.get('casual_leave')
        sick_leave = request.POST.get('sick_leave')
        maternity_leave = request.POST.get('maternity_leave')
        leave_reason = request.POST.get('leave_reason')
        leavefrom = request.POST.get('leavefrom')
        leaveto = request.POST.get('leaveto')
        leave_days = request.POST.get('leave_days')
        if earned_leave and not casual_leave and not sick_leave and not maternity_leave:
            if int(employee.cf) < int(leave_days):
                return render(request, 'leave_application.html', {'employee': employee, 'lowcfs': 'lowcfs'})
            else:
                try:
                    employee.cf = employee.cf - int(leave_days)
                    employee.save()
                    return render(request, 'leave_application.html', {'employee': employee})
                except Exception as e:
                    print(e)
                    return render(request, 'leave_application.html', {'employee': employee, 'exception': e})

        elif earned_leave:
            pass

        return render(request, 'leave_application.html', {'employee': employee})
    else:
        return render(request, 'leave_application.html', {'employee': employee})


def employee_logout(request):
    del request.session['emp_id']
    return render(request, 'index.html')
