from django.shortcuts import render

from core.models import Post


def indexView(request):
    posts = Post.objects.all()

    context = {
        "posts": posts,
    }

    return render(request, 'index.html', context)


def articleView(request, slug):
    post = Post.objects.get(slug=slug)

    context = {
        "post": post
    }
    return render(request, 'article.html', context)
