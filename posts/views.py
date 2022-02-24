from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import markdown

from .models import Post

def show(request, slug):
    post = Post.objects.filter(slug=slug).values("id", "title", "body", "created_at").first()

    if post is None:
        raise Http404("Post not Found")
    
    md = markdown.Markdown(extensions=['fenced_code'])
    md_content = md.convert(post.get("body"))

    title = post.get("title")

    return render(request, "show.html", {"post": {**post, 'body': md_content}, "title": title})

def index(request):
    page = request.GET.get('page', 1)

    posts = Post.objects.all().only("id", "title", "created_at", "description", "slug").order_by("-created_at")
    paginator = Paginator(posts, 8)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "index.html", {
        "posts": posts,
    })

def search(request):
    query_string = request.GET.get("search", "")
    posts = Post.objects.filter(title__icontains=query_string)

    paginator = Paginator(posts, 8)
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "search.html", {
        "posts": posts,
        "query_string": query_string
    })

def about(request):
    return render(request, "about.html")