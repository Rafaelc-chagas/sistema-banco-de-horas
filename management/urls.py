from django.urls import path
from . import views


urlpatterns = [
    path('management/', views.ManagementListView.as_view(), name='management_list'),
    path('management/<int:pk>/', views.ManagementDetailView.as_view(), name='management_detail'),
    path(
        'management/<int:pk>/list', views.ManagementEmployeesRegistryListView.as_view(),
        name='management_list_registry'
    )
]
