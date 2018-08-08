from django.shortcuts import render
from .models import Business

# Create your views here.


def home(request):
    
    return render(request, 'invest.html')


def invest(request):
    jpg=Business.get_all()
    return render(request, 'gjenge.html', {"jpg":jpg})