from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, CompanyProfile
from .forms import Profile, Company


@login_required
def company_profile(request):
    """ view to create user profile """

    if request.method == "POST":
        form = Company(request.POST)
        if form.is_valid():
            form.save()
            return(redirect('home'))

    else:
        form = Company()

    template = 'profiles/company_profile.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def user_profile(request):
    """ view to create user profile """

    if request.method == "POST":
        form = Profile(request.POST)
        if form.is_valid():
            form.save()
            return(redirect('home'))

    else:
        form = Profile()

    template = 'profiles/user_profile.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def profiles(request):
    """ View to render profile pages """

    return render(request, 'profiles/profile.html')

# NEW CODE SINCE DEPLOYMENT

# @login_required
# def profiles(request, profile):
#     """ View to render profile pages """

#     template = 'profiles/profile.html'

#     context = {
#     }

#     return render(request, template, context)
