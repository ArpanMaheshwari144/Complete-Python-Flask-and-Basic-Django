from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def removepunc(request):
    # Get the text
    text1=request.GET.get('text', 'default')
    print(text1)
    # Analyze the text
    return HttpResponse("remove punctuations <a href='/'>Go To Home</a>")

def capfirst(request):
    return HttpResponse("capitalize first <a href='/'>Go To Home</a>")

def newlineremove(request):
    return HttpResponse("new line remove <a href='/'>Go To Home</a>")

def spaceremove(request):
    return HttpResponse("space remover <a href='/'>Go To Home</a>")

def charcount(request):
    return HttpResponse("characters count <a href='/'>Go To Home</a>")