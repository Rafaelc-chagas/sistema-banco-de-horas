from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView, ListView
from accounts.models import EmployeeUser


class ManagementListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = EmployeeUser
    template_name = 'management_list.html'
    context_object_name = 'employees'
    permission_required = 'accounts.view_employeeuser'
    raise_exception = True


class ManagementDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = EmployeeUser
    template_name = 'management_detail.html'
    context_object_name = 'employee'
    permission_required = 'accounts.view_employeeuser'
    raise_exception = True
