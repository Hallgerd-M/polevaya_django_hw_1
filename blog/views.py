from blog.models import Post
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_tag=True)


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    model = Post
    fields = ("heading", "content", "preview")
    success_url = reverse_lazy('blog:post_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ("heading", "content", "preview")
    success_url = reverse_lazy('blog:post_list')

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', args=[self.kwargs.get('pk')])


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")
