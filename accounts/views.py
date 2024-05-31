from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from .forms import CPFLoginForm


class CPFLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CPFLoginForm


def logout_view(request):
    logout(request)
    return redirect('home')
