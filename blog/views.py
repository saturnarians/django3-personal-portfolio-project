from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.


def all_blogs(request):
    # To count how many blogs are there 
    #blog_count = Blog.objects.count

    # To show all blogs
    #blogs= Blog.objects.all()

    #For recent ones to show and Top 5
    blogs= Blog.objects.order_by('-date')[:5] 
    
    return render(request, 'blog/all_blogs.html',{'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
    #return render(request, 'blog/detail.html', {'id':blog_id})