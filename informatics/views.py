from itertools import chain

from django.shortcuts import render, redirect
from .models import TextContent, DocumentContent, Content, ContentManager, Event

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
    event = Event.objects.all()
    context = {"event": event}
    return render(request, 'events.html', context)

def addEvent(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        day = request.POST.get('day')

        # Save the new event
        Event.objects.create(
            name=name,
            image=image,
            description=description,
            day=day
        )
        return redirect('events')

    # Fetch all events to display in the table
    data = Event.objects.all()
    context = {"data": data}
    return render(request, 'add_event.html', context)

def update_event(request, id):
    try:
        edit = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return redirect('events')  # Redirect if the event doesn't exist.

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        day = request.POST.get('day')

        # Validate data
        if all([name, description, image, day]):
            edit.name = name
            edit.description = description
            edit.image = image
            edit.day = day
            edit.save()
            return redirect('events')

    context = {'d': edit}
    return render(request, 'update_event.html', context)

def delete_event(request, id):
    d = Event.objects.get(id=id)
    d.delete()
    return redirect('/events/')

def lecturers(request):
    return render(request, 'lecturers.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def businessIntelligence(request):
    course_name = "Business Intelligence"
    notes = chain(
        TextContent.objects.filter(course__name=course_name, content_type='NOTE'),
        DocumentContent.objects.filter(course__name=course_name, content_type='NOTE')
    )
    assignments = chain(
        TextContent.objects.filter(course__name=course_name, content_type='ASSIGNMENT'),
        DocumentContent.objects.filter(course__name=course_name, content_type='ASSIGNMENT')
    )
    cats = chain(
        TextContent.objects.filter(course__name=course_name, content_type='CAT'),
        DocumentContent.objects.filter(course__name=course_name, content_type='CAT')
    )
    context = {
        'notes': notes,
        'assignments': assignments,
        'cats': cats
    }
    return render(request, 'business-intelligence.html', context)

def computerNetworks(request):
    course_name = "Computer Networks"
    notes = chain(
        TextContent.objects.filter(course__name=course_name, content_type='NOTE'),
        DocumentContent.objects.filter(course__name=course_name, content_type='NOTE')
    )
    assignments = chain(
        TextContent.objects.filter(course__name=course_name, content_type='ASSIGNMENT'),
        DocumentContent.objects.filter(course__name=course_name, content_type='ASSIGNMENT')
    )
    cats = chain(
        TextContent.objects.filter(course__name=course_name, content_type='CAT'),
        DocumentContent.objects.filter(course__name=course_name, content_type='CAT')
    )
    context = {
        'notes': notes,
        'assignments': assignments,
        'cats': cats
    }
    return render(request, 'computer-networks.html', context)

def fose(request):
    course_name = "Fundamentals of Software Engineering"
    notes = chain(
        TextContent.objects.filter(course__name=course_name, content_type='NOTE'),
        DocumentContent.objects.filter(course__name=course_name, content_type='NOTE')
    )
    assignments = chain(
        TextContent.objects.filter(course__name=course_name, content_type='ASSIGNMENT'),
        DocumentContent.objects.filter(course__name=course_name, content_type='ASSIGNMENT')
    )
    cats = chain(
        TextContent.objects.filter(course__name=course_name, content_type='CAT'),
        DocumentContent.objects.filter(course__name=course_name, content_type='CAT')
    )
    context = {
        'notes': notes,
        'assignments': assignments,
        'cats': cats
    }
    return render(request, 'fose.html', context)

def greenComputing(request):
    course_name = "Green Computing"
    notes = chain(
        TextContent.objects.filter(course__name=course_name, content_type='NOTE'),
        DocumentContent.objects.filter(course__name=course_name, content_type='NOTE')
    )
    assignments = chain(
        TextContent.objects.filter(course__name=course_name, content_type='ASSIGNMENT'),
        DocumentContent.objects.filter(course__name=course_name, content_type='ASSIGNMENT')
    )
    cats = chain(
        TextContent.objects.filter(course__name=course_name, content_type='CAT'),
        DocumentContent.objects.filter(course__name=course_name, content_type='CAT')
    )
    context = {
        'notes': notes,
        'assignments': assignments,
        'cats': cats
    }
    return render(request, 'green-computing.html', context)

# def operatingSystems(request):
#     course_name = "Operating Systems"
#     contents = chain(
#         TextContent.objects.filter(course__name=course_name),
#         DocumentContent.objects.filter(course__name=course_name)
#     )
#     context = {'contents': contents}
#     return render(request, 'operating-systems.html', context)

def operatingSystems(request):
    course_name = "Operating Systems"
    notes = chain(
        TextContent.objects.filter(course__name=course_name, content_type='NOTE'),
        DocumentContent.objects.filter(course__name=course_name, content_type='NOTE')
    )
    assignments = chain(
        TextContent.objects.filter(course__name=course_name, content_type='ASSIGNMENT'),
        DocumentContent.objects.filter(course__name=course_name, content_type='ASSIGNMENT')
    )
    cats = chain(
        TextContent.objects.filter(course__name=course_name, content_type='CAT'),
        DocumentContent.objects.filter(course__name=course_name, content_type='CAT')
    )
    context = {
        'notes': notes,
        'assignments': assignments,
        'cats': cats
    }
    return render(request, 'operating-systems.html', context)

def programming2(request):
    course_name = "Programming For The Internet And Mobile Devices"
    notes = chain(
        TextContent.objects.filter(course__name=course_name, content_type='NOTE'),
        DocumentContent.objects.filter(course__name=course_name, content_type='NOTE')
    )
    assignments = chain(
        TextContent.objects.filter(course__name=course_name, content_type='ASSIGNMENT'),
        DocumentContent.objects.filter(course__name=course_name, content_type='ASSIGNMENT')
    )
    cats = chain(
        TextContent.objects.filter(course__name=course_name, content_type='CAT'),
        DocumentContent.objects.filter(course__name=course_name, content_type='CAT')
    )
    context = {
        'notes': notes,
        'assignments': assignments,
        'cats': cats
    }
    return render(request, 'programming2.html', context)

def sas311(request):
    course_name = "Ethics, Integrity And Social Responsibility"
    notes = chain(
        TextContent.objects.filter(course__name=course_name, content_type='NOTE'),
        DocumentContent.objects.filter(course__name=course_name, content_type='NOTE')
    )
    assignments = chain(
        TextContent.objects.filter(course__name=course_name, content_type='ASSIGNMENT'),
        DocumentContent.objects.filter(course__name=course_name, content_type='ASSIGNMENT')
    )
    cats = chain(
        TextContent.objects.filter(course__name=course_name, content_type='CAT'),
        DocumentContent.objects.filter(course__name=course_name, content_type='CAT')
    )
    context = {
        'notes': notes,
        'assignments': assignments,
        'cats': cats
    }
    return render(request, 'sas311.html', context)

def pricing(request):
    return render(request, 'pricing.html')