from django.urls import path

from informatics import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    path('lecturers/', views.lecturers, name='lecturers'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('business-intelligence/', views.businessIntelligence, name='business-intelligence'),
    path('computer-networks/', views.computerNetworks, name='computer-networks'),
    path('fundamentals-of-software-engineering/', views.fose, name='fose'),
    path('green-computing/', views.greenComputing, name='green-computing'),
    path('operating-systems-2/', views.operatingSystems, name='operating-systems'),
    path('programming2/', views.programming2, name='programming2'),
    path('ethics-integrity-and-social-responsibility/', views.sas311, name='sas311'),
    path('pricing/', views.pricing, name='pricing'),
]