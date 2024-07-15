from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404 , render

from .models import TeamNews , TeamGallery , TeamPlayer , TeamShop
from .forms import ShopCommentForm

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
    paginate_by = 6
    context_object_name = 'products'

class WeblogPageView(generic.ListView):
    model = TeamNews
    paginate_by = 6
    template_name = 'page_team/weblog.html'
    context_object_name = 'news'

# class PostDetailShopView(generic.DetailView):
#     model = TeamShop
#     template_name = 'page_team/post_detail.html'
#     context_object_name = 'shop'

def shop_details(request , pk):
    shop = get_object_or_404(TeamShop , pk = pk)
    shop_comment = shop.comments.all()

    if request.method == 'POST':
        comment_form = ShopCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.shop = shop
            comment.save()
            comment_form = ShopCommentForm()
    else:
        comment_form = ShopCommentForm()

    return render(request , 'page_team/post_detail.html' , {
        'shop' : shop,
        'comments' : shop_comment,
        'comment_form' : comment_form})