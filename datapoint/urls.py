"""
URL configuration for datapoint project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from employee import views as emp_views
from administration import views as adminViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', emp_views.index, name='index'),
    path('employee_overview/', emp_views.employee_overview,
         name='employee_overview'),
    path('employee_portfolio/', emp_views.employee_portfolio,
         name='employee_portfolio'),
    path('leave_application', emp_views.leave_application,
         name='leave_application'),
    path('leaveform_submit', emp_views.leaveform_submit, name='leaveform_submit'),
    path('', emp_views.employee_logout, name='employee_logout'),


    path('DatapointAdmin', adminViews.DatapointAdmin, name='datapoint_admin'),
    path('AdminLogin', adminViews.AdminLogin, name='admin_login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)