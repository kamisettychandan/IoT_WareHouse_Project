# API view for Sensor data
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TemperatureData

# User Login
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect




# API view for Sensor data section
@api_view(['GET'])
def get_temperature_data(request):
    data = TemperatureData.objects.all().order_by('-timestamp')[:100]
    result = [{"sensor": temp.sensor.name, "temperature": temp.temperature, "timestamp": temp.timestamp} for temp in data]
    return Response(result)

# User Login section
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')