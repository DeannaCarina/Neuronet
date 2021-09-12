from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, CompanyProfile
from .forms import Profile, Company


@login_required
def create_profile(request, form_type):
    """ view to create user profile """

    # Check to see if form is userProfile or companyProfile
    if form_type == 'userProfile':

        if request.method == "POST":
            form = Profile(request.POST)
            if form.is_valid():
                form.save()
                return(redirect('profiles'))

        else:
            form = Profile()

    elif form_type == 'companyProfile':

        if request.method == "POST":
            form = Company(request.POST)
            if form.is_valid():
                form.save()
                return(redirect('home'))

        else:
            form = Company()

    template = 'profiles/create_profile.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def profiles(request, profile):
    """ View to render profile pages """

    template = 'profiles/profile.html'

    context = {
    }

    return render(request, template, context)
