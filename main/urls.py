from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('buy/<int:id>', views.buy),
]
