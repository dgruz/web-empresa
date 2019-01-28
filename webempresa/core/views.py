from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    return render(request,"core/home.html")

def historia(request):
    return render(request,"core/historia.html")

def visitanos(request):
    return render(request,"core/store.html")

