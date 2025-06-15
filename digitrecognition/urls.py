from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('digitreco/', views.digitreco, name='digitreco'),
    path('predict/', views.predict, name='predict'),
]