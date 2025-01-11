import random
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def get_dashboard(request):
   data = {
      'temperature': round(random.uniform(20.0, 30.0), 2),
      'humidity': round(random.uniform(40.0, 60.0), 2),
    }
   return JsonResponse(data)

def dashboard_view(request):
    return render(request, 'dashboard.html')  # Kiểm tra tên file template chính xác



