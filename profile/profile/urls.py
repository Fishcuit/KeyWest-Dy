"""
Definition of urls for profile.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from app import forms, views


urlpatterns = [
    path('', views.index, name='home'),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)