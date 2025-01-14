from django.shortcuts import render, redirect ,reverse
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

#CRUD Create Red Update and Read

class LandingPageView(TemplateView):
    template_name = "landing.html"


class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = 'leads'


class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = 'lead'

class LeadCreateView(CreateView):
    template_name ='leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_list")


#def LandingPage(request):
#    return render(request, "landing.html")




def LeadList(request):
    
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)


class LeadUpdateView(UpdateView):

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