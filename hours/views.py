from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils import timezone
from django.views.generic import CreateView, ListView
from .forms import RegistryHoursForm
from .models import RegistryHours


class RegisterHoursCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = RegistryHours
    form_class = RegistryHoursForm
    template_name = 'register_hours.html'
    success_url = '/app/hours_report/'
    permission_required = 'hours.add_registryhours'
    raise_exception = True

    def form_valid(self, form):
        # Obtém a data atual
        today = timezone.now().date()

        # Verifica se o usuário já possui dois registros para o dia atual
        user_records_today = RegistryHours.objects.filter(employee=self.request.user, date=today).count()

        # Se o usuário já tiver dois registros para hoje, exibe uma mensagem de erro
        if user_records_today >= 2:
            form.add_error(None, "Você já possui dois registros para hoje.")
            return self.form_invalid(form)

        # Define o usuário no registro de horas e salva o formulário normalmente
        form.instance.employee = self.request.user
        return super().form_valid(form)


class HoursReportListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = RegistryHours
    template_name = 'hours_report.html'
    context_object_name = 'hours'
    permission_required = 'hours.view_registryhours'
    raise_exception = True

    def get_queryset(self):
        hours = super().get_queryset().filter(employee=self.request.user)
        return hours

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajuste para obter apenas o usuário logado, não precisa filtrar EmployeeUser
        context['employee'] = self.request.user
        return context
