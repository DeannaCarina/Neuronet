from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('create_profile/', views.create_profile, name='create_profile')
]
