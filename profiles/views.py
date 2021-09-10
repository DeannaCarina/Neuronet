from django.shortcuts import render


def profiles(request):
    """ View to render profile pages """

    return render(request, 'profiles/profile.html')
