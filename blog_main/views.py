
from django.shortcuts import render
from blogs.models import Blog,category

def home(request):
    
    featured_posts=Blog.objects.filter(is_featured=True,status='Published').order_by('-updated_at')
    #featured_postss=Blog.objects.filter(is_featured=True)
    posts=Blog.objects.filter(status='Published',is_featured=False)
    context={
        
        'featured_posts':featured_posts,
       # 'featured_postss':featured_postss,
       'posts':posts,

    }
    return render(request,'home.html',context)