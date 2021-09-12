from django.shortcuts import render
from itertools import chain
from profiles.models import UserProfile, CompanyProfile


def index(request):
    """ A view to return the index page """
    profiles = UserProfile.objects.all()
    companies = CompanyProfile.objects.all()
    all_profiles = list(chain(profiles, companies))

    template = 'home/index.html'

    context = {
        'all_profiles': all_profiles,
    }

    return render(request, template, context)
