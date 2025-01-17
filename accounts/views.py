from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import  generic

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
