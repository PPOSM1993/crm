from django.contrib import admin
from django.urls import path, include
from apps.leads.views import LandingPage


urlpatterns = [
    path('admin/', admin.site.urls),
    path("leads/", include("apps.leads.urls", namespace="leads")),
    path('', LandingPage, name="landing_page")
]
