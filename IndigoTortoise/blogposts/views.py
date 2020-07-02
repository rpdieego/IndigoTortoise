from django.shortcuts import render, redirect
from .models import ArticlesDb
from .forms import ArticlesForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

'''

'''

def articles(request):

    if request.method == 'POST':
        form = ArticlesForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_articles = ArticlesDb.objects.all
            messages.success(request,('New item added succesefully!'))
            return render(request, 'articles.html', {'all_articles':all_articles})

    else:
        all_articles = ArticlesDb.objects.all
        return render(request, 'articles.html', {'all_articles':all_articles})


def delete(request, art_id):
    article = ArticlesDb.objects.get(pk=art_id)
    article.delete()
    messages.success(request, ('Item deleted ..'))
    return redirect('articles')
