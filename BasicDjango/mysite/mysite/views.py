from django.http import HttpResponse
from django.shortcuts import render

# Basic:
def index(request):
    # params = {'name': 'arpan', 'place': 'USA'}
    # return render(request, 'index.html', params)
    return HttpResponse("Arpan")



def about(request):
    # params = {'name': 'adarsh', 'place': 'USA'}
    # return render(request, 'index.html', params)
    return HttpResponse("Adarsh")


def contact(request):
    # params = {'name': 'verma', 'place': 'USA'}
    # return render(request, 'index.html', params)
    return HttpResponse("<h1>Verma</h1>")
