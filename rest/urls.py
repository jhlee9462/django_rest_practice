from django.urls import path
from . import views

urlpatterns = [
    path('rest/', views.temp_here, name='temp_here'),
    path('rest/discover', views.temp_somewhere, name='temp_somewhere'),
]