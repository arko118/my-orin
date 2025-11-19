from django.urls import path
from . import views

urlpatterns = [
    path('', views.prf, name='home'),
]
