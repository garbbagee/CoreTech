from django.shortcuts import render

def index(request):
    context = {}
    return render(request,'html/index.html',context)