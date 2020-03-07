from django.shortcuts import render

# Create your views here.
def intercepter(func):
    def pre_process(request):
        func_name = str(func).split(" ")[1]
        print(func_name)
        return func(request)
    return pre_process


def show_home(request):
    request.session['name'] = "ttkc1018"
    ctx = {
        "current":"home"
    }
    return render(request, "home.html", ctx)

def show_news(request):
    ctx = {
        "current":"news"
    }
    return render(request, "news.html", ctx)

def show_about(request):
    ctx = {
        "current":"about"
    }
    return render(request, "about.html", ctx)

def show_blog(request):
    ctx = {
        "current":"blog"
    }
    return render(request, "blog.html", ctx)

def show_access(request):
    ctx = {
        "current":"access"
    }
    return render(request, "blog.html", ctx)

def show_other(request):
    cxt = {
        "current":"other",
        "name":"Guest",
        "chat":"chat",
    }
    return render(request, "chat.html", cxt)