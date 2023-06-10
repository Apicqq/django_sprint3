from datetime import datetime as dt

from blog.models import Category, Post
from django.db.models import Q
from django.shortcuts import get_object_or_404, render


def index(request):
    post_list = Post.objects.select_related('category').filter(
        Q(is_published=True)
        & Q(pub_date__lte=dt.now())
        & Q(category__is_published=True)
    )[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def category_posts(request, category_slug):
    post_list = Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        category__slug=category_slug,
        is_published=True,
        pub_date__lte=dt.now()
    )
    category = get_object_or_404(Category.objects.values(
        'title', 'description'
    ).filter(is_published=True), slug=category_slug)
    context = {'post_list': post_list, 'category': category}
    return render(request, 'blog/category.html', context)


def post_id(request, pk):
    post = get_object_or_404(Post.objects.filter(
        is_published=True,
        pub_date__lte=dt.now(),
        category__is_published=True),
        pk=pk
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)
