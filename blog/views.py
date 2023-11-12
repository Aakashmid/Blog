from blog.templatetags import extras
from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from blog.models import Post,blogComment
from django.contrib.auth.models import User
# Create your views here.

def BlogHome(request):

        allPost=Post.objects.all()
        context={'allPost':allPost}
        

        return render(request,'blog/blogHome.html',context)
        # return redirect(request,'home/')
def BlogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()  #Return first blog from list of blogs
    user=request.user    #Give current user 

    Comments=blogComment.objects.filter(post=post,parent=None)
    replies=blogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
             replyDict[reply.parent.sno].append(reply)
            
        
                
              
    context={'post':post,'comments':Comments,'user':user,'replyDict':replyDict}
    return render(request,'blog/blogPost.html',context)
def postComment(request):
      if request.method=='POST':
            postSno=request.POST.get('postSno')
            comment=request.POST.get('comment')
            post=Post.objects.get(sno=postSno)  #taking post by post no 
            parentSno=request.POST.get('parentSno')   #it is the sno of comment on which reply is done
            user=request.user
            
            if parentSno =="":
                  
                comment=blogComment(user=user,comments=comment,post=post)
                comment.save()
                messages.success(request,'comment is successfuly posted !!')
            else:
                parent=blogComment.objects.get(sno=parentSno)
                comment=blogComment(user=user,comments=comment,post=post,parent=parent)
                
                comment.save()
                messages.success(request,'Reply  is successfuly posted !!')

            # fetching all comments by post
            # Comments=blogComment.objects.filter(post=post)
            # return redirect('/')  #redirect to homepage
            
            return redirect(f'/blog/{post.slug}')
            