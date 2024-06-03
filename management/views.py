from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models.query import QuerySet
from django.views.generic import DetailView, ListView
from accounts.models import EmployeeUser
from hours.models import RegistryHours


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


class ManagementEmployeesRegistryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = RegistryHours
    template_name = 'hours_report_employee.html'
    context_object_name = 'hours'
    permission_required = 'accounts.view_employeeuser'
    raise_exception = True

    def get_queryset(self):
        employee_id = self.kwargs.get('pk')
        queryset = RegistryHours.objects.filter(employee=employee_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajuste para obter apenas o usuário logado, não precisa filtrar EmployeeUser
        employee = EmployeeUser.objects.get(id=self.kwargs.get('pk'))
        context['employee'] = employee
        return context
