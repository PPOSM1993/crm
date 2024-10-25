from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path("", views.HomePage, name="home_page"),
    path("lead_detail/<pk>/", views.LeadDetial, name="lead_detail")
]
