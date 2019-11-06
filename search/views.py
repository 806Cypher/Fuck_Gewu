from django.shortcuts import render
from django.http import HttpResponse
from . import fuck


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at fucking index")

def fuck(request):
    return HttpResponse("fuck")

