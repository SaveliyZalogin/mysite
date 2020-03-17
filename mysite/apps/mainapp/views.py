from django.shortcuts import render
from .models import News
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect


def login(request):
    if auth.user_logged_in:
        return HttpResponseRedirect('/main/')
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/main/")
    else:
        return HttpResponseRedirect("")


def logout(request):
    auth.logout(request)


def startpage(request):
    context = {


    }
    return render(request, "hello.html", context)


def index(request):
    newses = News.objects.all()
    context = {
        'newses': newses,
    }
    return render(request, "index.html", context)


def news(request, news_id):
    news = News.objects.get(id=news_id)
    context = {
        'new': news,

    }
    return render(request, "news.html", context)


def about(request):
    context = {


    }
    return render(request, "about.html", context)