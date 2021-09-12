from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('create_profile/form_type/', views.create_profile,
         name='create_profile')
]
