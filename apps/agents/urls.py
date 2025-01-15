from django.urls import path
from . import views

app_name = "agents"


urlpatterns = [
    path('', views.HelloWorld, name='hello_world')
]
