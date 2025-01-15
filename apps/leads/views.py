from django.shortcuts import render, redirect ,reverse
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.core.mail import send_mail

from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#CRUD Create Red Update and Read


class SignUpView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = 'leads'


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = 'lead'

class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    template_name ='leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_list")

    def form_valid(self, form):
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="posoriosanmartin@gmail.com",
            recipient_list=["pposm1.9.9.3soorio@gmail.com"]
        )
        return super(LeadCreateView, self).form_valid(form)

#def LandingPage(request):
#    return render(request, "landing.html")




def LeadList(request):
    
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)


class LeadUpdateView(LoginRequiredMixin, UpdateView):

    template_name = 'leads/lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_list")


#def LeadDetial(request, pk):
#    lead = Lead.objects.get(id=pk)
#    context = {
#        "lead": lead
#    }
#    return render(request, "leads/lead_detail.html", context)


#def LeadCreate(request):
#    form = LeadModelForm()
#    if request.method == "POST":
#        form = LeadModelForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect("/leads")

#    context = {
#        "form": form
#    }
#    return render(request, "leads/lead_create.html", context)



"""def LeadUpdate(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save() 

    context = {
        "form": form,
        "lead": lead
    }

    return render(request,"leads/lead_update.html", context)"""

class LeadDeleteView(DeleteView):
    template_name ='leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list')

"""def LeadDelete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')"""