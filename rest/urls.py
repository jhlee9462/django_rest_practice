from django.urls import path
from . import views

urlpatterns = [
    path('rest/', views.temp_here, name='temp_here'),
]