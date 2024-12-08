from django.urls import path

from informatics import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    path('add-event/', views.addEvent, name='add-event'),
    path('delete_event/<id>/', views.delete_event, name='delete_event'),
    path('update_event/<id>/', views.update_event, name='update_event'),
    path('lecturers/', views.lecturers, name='lecturers'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('business-intelligence/', views.businessIntelligence, name='business-intelligence'),
    path('computer-networks/', views.computerNetworks, name='computer-networks'),
    path('fundamentals-of-software-engineering/', views.fose, name='fose'),
    path('green-computing/', views.greenComputing, name='green-computing'),
    path('operating-systems-2/', views.operatingSystems, name='operating-systems'),
    path('programming2/', views.programming2, name='programming2'),
    path('ethics-integrity-and-social-responsibility/', views.sas311, name='sas311'),
    path('add-content/', views.add_content, name='add-content'),
    path('pay/', views.pay, name='pay'),
    path('token/', views.token, name='token'),
    path('pricing/', views.pricing, name='pricing'),
    path('stk/', views.stk, name="stk")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)