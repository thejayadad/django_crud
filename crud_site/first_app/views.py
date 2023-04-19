from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    my_dict = {'insert_me': 'Hello Im from views.py'}
    return render(request,'index.html', context=date_dict)
