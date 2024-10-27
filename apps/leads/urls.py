from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path("", views.HomePage, name="home_page"),
    path("lead_detail/<int:pk>/", views.LeadDetial, name="lead_detail"),
    path("lead_create/", views.LeadCreate, name="lead_create"),
    path("lead_update/<int:pk>/", views.LeadUpdate, name="lead_update"),
    path("lead_delete/<int:pk>/", views.LeadDelete, name="lead_delete"),
]
