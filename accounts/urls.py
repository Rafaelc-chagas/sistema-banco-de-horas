from django.urls import path
from . import views


urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.CPFLoginView.as_view(), name='login'),
]
