from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from blog1.models import article,comment

# Create your views here.
def add(request):
    if request.method == "POST":
        title = request.POST.get('title',None)
        content = request.POST.get('content',None)
        new = article(title = title,content = content)
        new.save()
        return HttpResponseRedirect('/list/')
        
    return render(request,'add.html')


def list(request):
    articles = article.objects.order_by("-id").all()
    return render(request,'list.html',{'articles':articles})

def view(request,id):
    articless = article.objects.get(id=id)
    Comments = comment.objects.filter(article = id).order_by("-id").all()
    

    return render(request,'view.html',{'articless':articless,"Comments":Comments})
def comment_add(request):
    if request.method =="POST":
        detail = request.POST.get('detail',None)
        article_id = request.POST.get('article',None)
        if article_id and detail:
            Comment = comment()
            Comment.article = article(id=article_id )
            Comment.detail = detail
            Comment.save()
        print(article_id)
        return HttpResponseRedirect('/view/%s'%article_id)
        
    
