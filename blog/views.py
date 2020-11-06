from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def display_blogcontent(request):
    blogposts = BlogPost.objects.all()
    template = 'blog/blog.html'
    context = {
        'blogposts': blogposts,
        }

    return render(request, template, context)


def show_post(request, slug):
    blogpost = get_object_or_404(BlogPost, slug=slug)
    template = 'show_post.html'
    context = {
        'blogpost': blogpost
        }
    return render(request, template, context)
