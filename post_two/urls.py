from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostListAPI,
    PostDetailAPI,
)

urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("detail/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("new/", PostCreateView.as_view(), name="post_create"),
    path("<int:pk>/edit", PostUpdateView.as_view(), name="post_update"),
    path("<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),
    path("api/v1/", PostListAPI.as_view(), name="post_list_api"),
    path("api/v1/<int:pk>", PostDetailAPI.as_view(), name="post_detail_api"),
]
