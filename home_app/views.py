from django.shortcuts import render
from blog_app.models import Article, Category

def home(request):
    article = Article.objects.all()
    recent_articles = Article.objects.all()[:3]
    
    context = {
        "article":article,
        
    }
    return render(request, 'home_app/index.html', context)
