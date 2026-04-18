
from django.shortcuts import redirect, render
from assignments.models import About
from blogs.models import Blog,category
from .forms import RegistrationForm 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
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
def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form=RegistrationForm()
    form=RegistrationForm()
    context={
        'form':form,
    }
    return render(request,'register.html',context)
def login(request):
    if request.method=='POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('home')
    form=AuthenticationForm()
    context={
        'form':form,
    }
    return render(request,'login.html',context)
def logout(request):
    auth.logout(request)
    return redirect('home')