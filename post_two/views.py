from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post_two
from django.urls import reverse_lazy
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PostSerializer

# Create your views here.
class PostListAPI(ListCreateAPIView):
    queryset = Post_two.objects.all()
    serializer_class = PostSerializer


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Post_two.objects.all()
    serializer_class = PostSerializer


class PostListView(ListView):
    template_name = "post-list.html"
    model = Post_two


class PostDetailView(DetailView):
    template_name = "post-detail.html"
    model = Post_two


class PostCreateView(CreateView):
    template_name = "post-create.html"
    model = Post_two
    fields = ["title", "author", "body"]


class PostUpdateView(UpdateView):
    template_name = "post-update.html"
    model = Post_two
    fields = ["title", "body"]


class PostDeleteView(DeleteView):
    template_name = "post-delete.html"
    model = Post_two
    success_url = reverse_lazy("list")
