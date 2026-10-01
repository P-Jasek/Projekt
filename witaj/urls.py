from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='strona_glowna'), # Działa dla samego pi26pjasek.pythonanywhere.com
    path('hello/', views.hello, name='hello'),   # Działa dla .../hello/
    path('hello_template/<str:name>/', views.hello_template, name='hello_template'),
]