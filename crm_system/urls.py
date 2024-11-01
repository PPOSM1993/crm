from django.contrib import admin
from django.urls import path, include
from apps.leads.views import LandingPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("leads/", include("apps.leads.urls", namespace="leads")),
    path('', LandingPageView.as_view(), name="landing_page")
]
