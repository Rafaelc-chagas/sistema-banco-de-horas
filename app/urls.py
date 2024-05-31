from django.contrib import admin
from django.urls import path, include
from .views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('accounts.urls')),
    path('app/', include('hours.urls')),
    path('app/', include('management.urls')),
    path('home/', HomeView.as_view(), name='home'),
]
