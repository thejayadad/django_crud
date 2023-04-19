from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_me': 'Hello Im from views.py'}
    return render(request,'index.html', context=my_dict)
