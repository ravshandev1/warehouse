from django.urls import path
from .views import WarehouseAPI

urlpatterns = [
    path('', WarehouseAPI.as_view())
]
