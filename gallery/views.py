from django.shortcuts import render

# Create your views here.
def App(request):
    return render(request, 'gallery/App.html')

def Website(request):
    return render(request, 'gallery/Website.html')

def System(request):
    return render(request, 'gallery/System.html')