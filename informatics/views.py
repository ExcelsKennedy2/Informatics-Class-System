from itertools import chain
import os
from django.shortcuts import render, redirect
from .models import TextContent, DocumentContent, Event, Course, Semester
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from . credentials import MpesaAccessToken, LipanaMpesaPpassword

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

def add_content(request):
    if request.method == 'POST':
        content_type = request.POST.get('content_type')
        title = request.POST.get('title')
        course_id = request.POST.get('course')
        semester_id = request.POST.get('semester')
        text = request.POST.get('text', '')
        uploaded_file = request.FILES.get('file')

        # Validate data (optional)

        if content_type in ('NOTE', 'CAT', 'ASSIGNMENT'):
            if text:
                # Create TextContent object (if text is provided)
                content = TextContent.objects.create(
                    content_type=content_type,
                    title=title,
                    course_id=course_id,
                    semester_id=semester_id,
                    text=text
                )
            elif uploaded_file:
                # Extract filename without extension
                filename, extension = os.path.splitext(uploaded_file.name)
                # Set the title to the filename without extension
                title = request.POST.get('title')

                # Create DocumentContent object (if file is uploaded)
                content = DocumentContent.objects.create(
                    content_type=content_type,
                    title=title,
                    course_id=course_id,
                    semester_id=semester_id,
                    file=uploaded_file
                )
            else:
                # Handle case where neither text nor file is provided
                pass  # You can add error handling here

        else:
            # Handle invalid content type (optional)
            pass

        return redirect('dashboard')  # Redirect to a success page (optional)

    courses = Course.objects.all()
    semesters = Semester.objects.all()
    context = {'courses': courses, 'semesters': semesters}
    return render(request, 'add_content.html', context)


def pay(request):
    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Excels Kennedy",
            "TransactionDesc": "Web Development Charges"
        }

    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse("success")

def token(request):
    consumer_key = 'KzFqHe8zMChJ5vs8qdIjSILn00MtMBJiY8qaq1NmhE8ApPXY'
    consumer_secret = 'pDVE5Xe2LlXAZrd1L38wF9vMBe0BELDcX89dL1Fu6jyYuiFn09iPixSLGBb6nAew'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def stk(request):
    return render(request, 'pay.html', {'navbar':'stk'})

def pricing(request):
    return render(request, 'pricing.html')

# Third Year Second Semester

def dses(request):
    course_name = "Decision Support and Expert Systems"
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
    return render(request, 'dses.html', context)

def hci(request):
    course_name = "Human-Computer Interaction"
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
    return render(request, 'hci.html', context)

def cyberLawAndEthics(request):
    course_name = "Cyber Law and Ethics"
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
    return render(request, 'cyber-law-and-ethics.html', context)

def biometricsAndCyberSecurity(request):
    course_name = "Biometrics and Cyber Security"
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
    return render(request, 'biometrics-and-cyber-security.html', context)

def cloudComputing(request):
    course_name = "Cloud Computing and Emerging Technologies"
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
    return render(request, 'cloud-computing.html', context)

def multimediaSystems(request):
    course_name = "Multimedia Systems and Animation Technologies"
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
    return render(request, 'multimedia-systems.html', context)

def dataScienceAndMachineLearning(request):
    course_name = "Data Science and Machine Learning"
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
    return render(request, 'data-science-and-machine-learning.html', context)