from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def valami(request):
    template = 'valami.html'
    context = {}
    return render(request,template,context)