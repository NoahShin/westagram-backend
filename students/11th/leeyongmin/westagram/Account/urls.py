from django.urls import path
from . import views

app_name='Account'

urlpatterns = [
    path('', views.SignUp.as_view()),
]
