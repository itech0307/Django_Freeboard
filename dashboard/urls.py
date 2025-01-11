from django.urls import path
from .views import get_dashboard
from .views import dashboard_view


urlpatterns = [
    path('data/', get_dashboard, name='get_data'),
    path('', dashboard_view, name='dashboard_view'),
]