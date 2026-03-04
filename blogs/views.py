from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Blog,category

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