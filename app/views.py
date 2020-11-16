from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from num2words import num2words

from app.forms import Number

def index(request):
    words=None
    if request.GET.get('num'):
        number = request.GET.get('num')
        words = num2words(number)

    return render(request, 'index.html',{
        'words': words,
    })