from django.views.generic import ListView,CreateView
from .models import Posts 
from django.urls import reverse_lazy
from .forms import PostForm


class Home(ListView):
    model = Posts
    template_name = "home.html"

class CreateForm(CreateView):
    model = Posts
    template_name = "post.html"
    form_class = PostForm
    success_url = reverse_lazy("home")
