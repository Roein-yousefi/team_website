from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404 , render

from .models import TeamNews

class HomePageView(generic.ListView):
    model = TeamNews
    template_name = 'page_team/home.html'
    context_object_name = 'items'
