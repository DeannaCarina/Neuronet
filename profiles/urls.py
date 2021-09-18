from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('company_profile/', views.company_profile,
         name='company_profile'),
    path('user_profile/', views.user_profile,
         name='user_profile'),
]
