from django.shortcuts import render
from .models import News, KeyWords
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SearchForm


def none_url(request):
    return HttpResponseRedirect('/login/')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/main/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'hello.html', {'form': form})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('http://127.0.0.1:8000')


def index(request):
    newses = News.objects.all()
    keywords = KeyWords.objects.all()
    context = {
        'newses': newses,
        'logout': logout,
    }
    return render(request, "index.html", context)


def search(request):
    try:
        search_query = request.GET.get('search', '')
        posts = News.objects.filter(title__icontains=search_query)
    except:
        search_query = ''

    context = {
        'post_list': posts
    }
    return render(request, "search.html", context)


def news(request, news_id):
    news = News.objects.get(id=news_id)
    keywords = KeyWords.objects.all()
    for keyword in keywords:
        if keyword in news.key_word.all():
            word = keyword
    context = {
        'new': news,
        'key': word,
        }
    return render(request, "news.html", context)


def about(request):
    context = {

    }
    return render(request, "about.html", context)
