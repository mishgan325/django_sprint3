from django.http import Http404
from django.shortcuts import render


def index(request):
    template = 'blog/index.html'
    context = {'posts': posts[::-1]}
    return render(request, template, context)


def post_detail(request, post_id):
    if post_id not in post_dict:
        raise Http404(f'Пост с id:{post_id} не найден')
    template = 'blog/detail.html'
    context = {'post': post_dict[post_id]}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template, context)
