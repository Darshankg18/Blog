from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, category
from django.contrib.auth.decorators import login_required

from dashboards.forms import CategoryForm

# Create your views here. 
@login_required(login_url='login')
def dashboard(request):
    category_count=category.objects.all().count()
    blogs_count=Blog.objects.all().count()

    context={
        'category_count':category_count,
        'blogs_count':blogs_count,
    }
    return render(request,'dashboard/dashboard.html',context)

def categories(request):
    return render(request,'dashboard/categories.html')

def add_category(request):
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm()
    context={
        'form':form,
    }
    return render(request,'dashboard/add_category.html',context)
def edit_category(request,pk):
    Category=get_object_or_404(category,pk=pk)
    if request.method=='POST':
        form = CategoryForm(request.POST,instance=Category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm(instance=Category)
    context={
        'form':form,
        'Category':Category,
    }
    return render(request,'dashboard/edit_category.html',context)
def delete_category(request,pk):
    Category=get_object_or_404(category,pk=pk)
    Category.delete()

    return redirect('categories')