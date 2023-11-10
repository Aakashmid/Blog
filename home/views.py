from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from blog.models import Post

# Create your views here.
def home(request):
    allPosts=Post.objects.all()

    somePost=[]
    for i in range(len(allPosts)):
        somePost.append(allPosts[i])
        if i==1:
            break


    return render(request,"home/index.html",{'Posts':somePost})
def about(request):
    return render(request,"home/about.html")
def contact(request):
    if request.method=='POST':
        
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone_no=request.POST.get('phone',0)
        desc=request.POST.get('desc','')

        if len(name)<4 or len(email)<3 or len(phone_no)<5:
            messages.error(request,"Fill form correctly ")
        else:
            messages.success(request,'Successfuly submitted')
        
            contact=Contact(name=name,email=email,phone_no=phone_no,desc=desc)
            contact.save()    
            return render(request,'home/contact.html')
    return render(request,'home/contact.html')

def search(request):
    query=request.GET.get('query')
    # if len(query)>45  or len(query)==0:
    #     return render(request,'home/search.html',{'query':query})
    
    # else:
    PostTitle=Post.objects.filter(title__icontains=query)
    PostContent=Post.objects.filter(content__icontains=query)
    blogs=PostTitle.union(PostContent)                              #Combining posts searched  by title and  content
    return render(request,'home/search.html',{'Posts':blogs,'query':query})

#handling sign up of user
def signUp(request):
    if request.method=='GET':
        lname=request.GET.get('lname')
        fname=request.GET.get('fname')
        username=request.GET.get('username')
        email=request.GET.get('email')
        password=request.GET.get('password')
        if  User.objects.filter(username=username).exists():
            messages.error(request,'This username is taken')
            return redirect ('/')
        
        else:
            # if password.isalnum() is False:
            #     messages


            user=User.objects.create_user(username=username,email=email,password=password)
            user.first_name=fname
            user.last_name=lname
            user.save()
            messages.success(request,'Account is created succefuly!!')
            return redirect('/')
    else:
        return redirect('/') 

# Handling login of user
def loginHand(request):
    if request.method=='GET':
        username=request.GET.get('username')
        password=request.GET.get('password')
        
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfuly login ')
            return redirect('/')
        else:
            messages.error(request,"username or password is wrong")
            return redirect('/')
        

def logoutHand(request):
    logout(request)
    messages.success(request,'Successfuly logout ')
    return redirect('/')

    