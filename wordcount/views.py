#need comment
from django.http import HttpResponse
#need comment
from django.shortcuts import render


#These are the functions that retrun the page/content based on the urls.py request
def home(request):
    return render(request, 'home.html')

def cars(request):
    return HttpResponse('I like cars')

def count(request):
    fulltext = request.Get['fulltext']
    return render(request, 'count.html', {'fulltext':fulltext})
