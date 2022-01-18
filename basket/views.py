from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def basket_summary(request):
    return render(request,'store/basket/basket_summary.html',{})