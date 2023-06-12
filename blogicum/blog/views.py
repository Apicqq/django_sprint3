from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now

from blog.models import Category, Post


def index(request):
    post_list = Post.objects.select_related(
        'category', 'author', 'location').filter(
        Q(is_published=True)
        & Q(pub_date__lte=now())
        & Q(category__is_published=True)
    )[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        is_published=True,
        slug=category_slug
    )

    post_list = category.posts.filter(
        is_published=True,
        pub_date__lte=now()
    )

    context = {'post_list': post_list, 'category': category}
    return render(request, 'blog/category.html', context)


def post_detail(request, pk):
    post = get_object_or_404(
        Post,
        is_published=True,
        pub_date__lte=now(),
        category__is_published=True,
        pk=pk
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)
