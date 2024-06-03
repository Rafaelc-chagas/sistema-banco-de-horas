from django.urls import path
from . import views


urlpatterns = [
    path('hours_report/', views.HoursReportListView.as_view(), name='hours_report'),
    path('register_hours/', views.RegisterHoursCreateView.as_view(), name='register_hours'),
    path('update/<int:pk>/', views.RegistryHoursUpdateView.as_view(), name='update_hours')
]
