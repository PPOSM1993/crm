from django.urls import path
from . import views
from .views import LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='lead_list'),
    path("lead_detail/<int:pk>/", LeadDetailView.as_view(), name="lead_detail"),
    path("lead_create/", LeadCreateView.as_view(), name="lead_create"),
    path("lead_update/<int:pk>/", LeadUpdateView.as_view(), name="lead_update"),
    path("lead_delete/<int:pk>/", LeadDeleteView.as_view(), name="lead_delete"),
]
