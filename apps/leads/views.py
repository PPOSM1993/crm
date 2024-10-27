from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def HomePage(request):
    
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/home_page.html", context)


def LeadDetial(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)


def LeadCreate(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            #first_name = form.cleaned_data["first_name"]
            #last_name = form.cleaned_data["last_name"]
            #age = form.cleaned_data["age"]
            #agent = form.cleaned_data["agent"]
            #agent = Agent.objects.first()
            #Lead.objects.create(
            #    first_name = first_name,
            #    last_name = last_name,
            #    age = age,
            #    agent = agent
            #)

            return redirect("/leads")

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)

"""def LeadUpdate(request, pk):

    lead = Lead.objects.get(id=pk)
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():

            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            age = form.cleaned_data["age"]

            lead.first_name = first_name
            lead.last_name = last_name
            lead.age = age

            lead.save()

            return redirect("/leads")
    
    context = {
        "form": form,
        "lead": lead
    }
    return render(request,"leads/lead_update.html", context)"""


def LeadUpdate(request, pk):
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

    return render(request,"leads/lead_update.html", context)

def LeadDelete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')