from django.shortcuts import redirect, render, get_object_or_404
from . models import Article, Category, Comment, Message
from django.core.paginator import Paginator
from .forms import ContactUsForm ,MessageForm

def post_detail(request, pk):
    articles = get_object_or_404(Article, id=pk)
    if request.method == "POST":
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body , article=articles, user=request.user, parent_id=parent_id)
    context={
        "articles":articles,
        
    }
    return render(request, "blog_app/post-details.html", context)
    
def post_list(request):
    articles_list = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles_list, 2)
    object_list = paginator.get_page(page_number)
    
    context ={
        "articles_list":object_list,
        
    }
    return render(request, "blog_app/post-lists.html", context)


def category_detail(request, pk):
    category = get_object_or_404(Category, id=pk)
    articles_list = category.article_set.all()
    context ={
        "articles_list":articles_list,
    }
    return render(request, "blog_app/post-lists.html", context)





def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    context={
        "articles_list": articles,
        
    }
    return render(request, "blog_app/post-lists.html",context)
    


   
def contact(request):
    if request.method == "POST":
        form = MessageForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            email = form.cleaned_data['email']
            Message.objects.create(title=title ,text=text, email=email                                                                                                                 )

            
    else:    
        form = MessageForm()
    context = {
        "form":form,
    }
    return render(request, "blog_app/contact.html", context)   
   
    
def about(request):
    return render(request, "blog_app/about_us.html")    