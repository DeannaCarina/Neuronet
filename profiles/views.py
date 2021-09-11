from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import Profile


@login_required
def create_profile(request):
    """ view to create user profile """

    if request.method == "POST":
        form = Profile(request.POST)
        if form.is_valid():
            form.save()
            return(redirect('profiles'))

    else:
        form = Profile()

    template = 'profiles/create_profile.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def profiles(request):
    """ View to render profile pages """

    return render(request, 'profiles/profile.html')
