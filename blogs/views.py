from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Blog,category
from django.db.models import Q

# Create your views here.
def posts_by_category(request,category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts=Blog.objects.filter(status='Published' , category_id=category_id)
    #use try & except when we want do custom actions if the the category does not exist
    # try:
    #     categoryy=category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')
    #use get_object_404() when we want to show 404 page if the category does not exist
    categoryy=get_object_or_404(category,pk=category_id)
    context={
        'categoryy':categoryy  ,
        'posts':posts,
        'category_id':category_id,
    }
    return render(request,'posts_by_category.html',context)

def blogs(request,slug):
    single_blog=get_object_or_404(Blog,slug=slug,status="Published")
    context={
        'single_blog':single_blog,
    }
    return render(request,'blogs.html',context)
def search(request):
    keyword=request.GET.get('keyword')
    blogs=Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) |Q(blog_body__icontains=keyword),status='Published')
    context={
        'blogs':blogs,
        'keyword':keyword,
    }
    return render(request,'search.html',context)