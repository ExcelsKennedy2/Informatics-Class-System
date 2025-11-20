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
    path('add-content/', views.add_content, name='add-content'),
    path('pay/', views.pay, name='pay'),
    path('token/', views.token, name='token'),
    path('pricing/', views.pricing, name='pricing'),
    path('stk/', views.stk, name="stk"),


   path('robotics/', views.course1, name='robotics'),
    path('artificial-intelligence/', views.course2, name='artificial-intelligence'),
    path('computer-graphics/', views.course3, name='computer-graphics'),
    path('network-design/', views.course4, name='network-design'),
    path('software-engineering/', views.course5, name='software-engineering'),
    path('information-security/', views.course6, name='information-security'),
    path('informatics-project-2/', views.course7, name='informatics-project-2'),
    path('entreprenuership-and-employability/', views.course8, name='entreprenuership-and-employability'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)