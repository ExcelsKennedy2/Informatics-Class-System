from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views
from .views import CustomLoginView, RegisterPage
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
]