from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Profile, Link


# Create your views here.
class LinkListView(ListView):
    model = Link


class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    success_url = reverse_lazy("link-list")


class LinkUpdateView(UpdateView):
    model = Link
    fields = ["text", "url"]
    success_url = reverse_lazy("link-list") 
