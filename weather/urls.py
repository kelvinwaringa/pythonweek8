from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Default route for the weather home.
]
