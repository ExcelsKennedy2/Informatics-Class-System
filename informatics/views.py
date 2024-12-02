from itertools import chain

from django.shortcuts import render
from .models import TextContent, DocumentContent, Content, ContentManager

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
    course_name = "Business Intelligence"
    contents = chain(
        TextContent.objects.filter(course__name=course_name),
        DocumentContent.objects.filter(course__name=course_name)
    )
    context = {'contents': contents}
    return render(request, 'business-intelligence.html', context)

def computerNetworks(request):
    course_name = "Computer Networks"
    contents = chain(
        TextContent.objects.filter(course__name=course_name),
        DocumentContent.objects.filter(course__name=course_name)
    )
    context = {'contents': contents}
    return render(request, 'computer-networks.html', context)

def fose(request):
    course_name = "Fundamentals of Software Engineering"
    contents = chain(
        TextContent.objects.filter(course__name=course_name),
        DocumentContent.objects.filter(course__name=course_name)
    )
    context = {'contents': contents}
    return render(request, 'fose.html', context)

def greenComputing(request):
    course_name = "Green Computing"
    contents = chain(
        TextContent.objects.filter(course__name=course_name),
        DocumentContent.objects.filter(course__name=course_name)
    )
    context = {'contents': contents}
    return render(request, 'green-computing.html', context)

def operatingSystems(request):
    course_name = "Operating Systems"
    contents = chain(
        TextContent.objects.filter(course__name=course_name),
        DocumentContent.objects.filter(course__name=course_name)
    )
    context = {'contents': contents}
    return render(request, 'operating-systems.html', context)

def programming2(request):
    course_name = "Programming For The Internet And Mobile Devices"
    contents = chain(
        TextContent.objects.filter(course__name=course_name),
        DocumentContent.objects.filter(course__name=course_name)
    )
    context = {'contents': contents}
    return render(request, 'programming2.html', context)

def sas311(request):
    course_name = "Ethics, Integrity And Social Responsibility"
    contents = chain(
        TextContent.objects.filter(course__name=course_name),
        DocumentContent.objects.filter(course__name=course_name)
    )
    context = {'contents': contents}
    return render(request, 'sas311.html', context)

def pricing(request):
    return render(request, 'pricing.html')