from django.shortcuts import render, get_object_or_404
from .models import Business, Entry
from .forms import BusinessForm

# Create your views here.


def home(request):
    
    return render(request, 'invest.html')


def invest(request):
    jpg=Business.get_all()
    if request.method=='POST':
        form=BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            investment=form.save(commit=False)
            investment.save()
    else:
        form=BusinessForm()
    return render(request, 'gjenge.html', {"jpg":jpg, "form":form})

