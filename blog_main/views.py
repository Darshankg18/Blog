
from django.shortcuts import render
from assignments.models import About
from blogs.models import Blog,category

def home(request):
    #categories=category.objects.all()
    featured_posts=Blog.objects.filter(is_featured=True,status='Published').order_by('-updated_at')
    #featured_postss=Blog.objects.filter(is_featured=True)
    posts=Blog.objects.filter(status='Published',is_featured=False)
    
    #Fetch about us
    try:
        about=About.objects.get()
    except:
        about=None
    context={
        #'categories':categories
        'featured_posts':featured_posts,
       # 'featured_postss':featured_postss,
       'posts':posts,
       'about':about,

    }
    return render(request,'home.html',context)