# Define URL Routes
from django.urls import path
from dashboard import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/temperature/', views.get_temperature_data, name='get_temperature_data'),
]
