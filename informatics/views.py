from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def events(request):
    return render(request, 'events.html')

def lecturers(request):
    return render(request, 'lecturers.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def businessIntelligence(request):
    return render(request, 'business-intelligence.html')

def computerNetworks(request):
    return render(request, 'computer-networks.html')

def fose(request):
    return render(request, 'fose.html')

def greenComputing(request):
    return render(request, 'green-computing.html')

def operatingSystems(request):
    return render(request, 'operating-systems.html')

def programming2(request):
    return render(request, 'programming2.html')

def sas311(request):
    return render(request, 'sas311.html')

def pricing(request):
    return render(request, 'pricing.html')