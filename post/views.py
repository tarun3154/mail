from django.shortcuts import render

from .models import *

def blog_list(request):
   posts = Post.objects.all()
   return render(request, 'post/base.html', {'posts': posts})

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post/blogdetail.html', {'post': post})
