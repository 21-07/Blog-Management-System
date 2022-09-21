from django.shortcuts import render,redirect
from blogapp.models import Blogs
from django.contrib.auth.forms import UserCreationForm
from blogapp.forms import CreateBlog, UpdateBlog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def home_view(request):
    return render(request,"blogapp/home.html")


@login_required
def index_view(request):
    try:
        context={
            'blogs':Blogs.objects.all()
        }
    except Exception as e:
        print(e)
    return render(request,'blogapp/index.html',context)


def user_view(request):
    try:
        form=UserCreationForm()
        if request.method=="POST":
            form=UserCreationForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
    except Exception as e:
        print(e)
    return render(request,"blogapp/register.html",{'form':form})

@login_required
def create_view(request):
    try:
        form=CreateBlog()
        if request.method=="POST":
            form=CreateBlog(request.POST,request.FILES)
            if form.is_valid():
                blog_obj=form.save(commit=False)
                blog_obj.user=request.user
                form.save()
            return redirect(f"/index/")    
    except Exception as e:
        print(e)            
    return render(request,"blogapp/create.html",{'form':form}) 

@login_required
def detail_view(request,id):
    obj=Blogs.objects.get(pk=id)
    return render(request,"blogapp/detail.html",{'obj':obj})

@login_required
def update_view(request,id):
    obj=Blogs.objects.get(pk=id)
    form=UpdateBlog(instance=obj)
    if request.method=="POST":
        form=UpdateBlog(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect(f'/detail/{obj.id}/')
    return render(request,"blogapp/update.html",{'obj':obj,'form':form}) 


@login_required
def delete_view(request,id):
    obj=Blogs.objects.get(pk=id)
    obj.delete()
    return redirect(f"/index/") 


@login_required
def user_blog_view(request,id):
    obj1=User.objects.get(pk=id)
    obj2=Blogs.objects.filter(user=obj1)
    return render(request,"blogapp/user.html",{'blogs':obj2})




        





