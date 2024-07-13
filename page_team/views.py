from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404 , render

from .models import TeamNews , TeamGallery , TeamPlayer , TeamShop

class HomePageView(generic.TemplateView):
    template_name = 'page_team/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model1 = TeamNews.objects.order_by('-datetime_created')[:3]


        context['model1'] = model1

        return context

class ShopPageView(generic.ListView):
    model = TeamShop
    template_name = 'page_team/shop.html'
    context_object_name = 'products'

class WeblogPageView(generic.ListView):
    model = TeamNews
    template_name = 'page_team/weblog.html'
    context_object_name = 'news'

