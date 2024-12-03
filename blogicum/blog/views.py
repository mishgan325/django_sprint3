from django.utils.timezone import now

from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Post, Category

from django.views.generic import DetailView, ListView


class IndexListView(ListView):
    template_name = 'blog/index.html'
    model = Post
    paginate_by = 5

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(
                is_published=True,
                pub_date__lte=now(),
                category__is_published=True,
            )
        )


class PostDetailView(DetailView):
    template_name = 'blog/detail.html'
    model = Post

    def get_object(self, queryset=None):
        # Получаем публикацию по ID
        post = get_object_or_404(
            Post,
            pk=self.kwargs.get('post_id'),
            is_published=True,
            pub_date__lte=now()
        )
        if not post.category.is_published:
            raise Http404("Category is not published")
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object
        return context


class CategoryDetailView(ListView):
    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        self.category = get_object_or_404(
            Category,
            slug=self.kwargs.get('category_slug'),
            is_published=True
        )

        return Post.objects.filter(
            category=self.category,
            is_published=True,
            pub_date__lte=now()
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
