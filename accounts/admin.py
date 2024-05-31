from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import EmployeeUserCreationForm, EmployeeUserChangeForm
from .models import EmployeeUser


class EmployeeUserAdmin(UserAdmin):
    add_form = EmployeeUserCreationForm
    form = EmployeeUserChangeForm
    model = EmployeeUser
    list_display = ['cpf', 'email', 'full_name', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('cpf', 'password')}),
        ('Informações Pessoais', {'fields': ('email', 'full_name')}),
        ('Permissões', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cpf', 'email', 'password1', 'password2', 'is_staff', 'is_active')}),
    )
    search_fields = ('cpf', 'email')
    ordering = ('cpf',)


admin.site.register(EmployeeUser, EmployeeUserAdmin)
