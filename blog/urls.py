from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostCreateView, PostUpdateView, PostListView, PostDetailView, PostDeteleView

app_name = BlogConfig.name

urlpatterns = [
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post_list/", PostListView.as_view(), name="post_list"),
    path("post_detail/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/delete/", PostDeteleView.as_view(), name="post_delete"),
]
