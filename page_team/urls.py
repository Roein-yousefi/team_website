from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('shop' , views.ShopPageView.as_view(), name='shop'),
    path('news' , views.WeblogPageView.as_view(), name='news'),
    path('team' , views.TeamPlayersView.as_view() , name='team'),
    path('shop/<int:pk>', views.shop_details , name='shop-detail'),
    path('news/<int:pk>', views.WeblogDetailView.as_view(), name='news_detail'),


]