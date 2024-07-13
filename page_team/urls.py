from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('shop' , views.ShopPageView.as_view(), name='shop'),
    path('news' , views.WeblogPageView.as_view(), name='news'),
]