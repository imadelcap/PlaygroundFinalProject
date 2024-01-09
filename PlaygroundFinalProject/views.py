from django.shortcuts import render
from django.template import loader


def inicio(request):
    return render(request, 'index.html',)

def about(request):
    return render(request, 'about.html')
