from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('signIn/', views.signin),
    path('signUp/',views.signup),
]