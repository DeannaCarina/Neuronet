# NEW CODE (DOESN'T WORK)

# from django.shortcuts import render
# from profiles.models import UserProfile, CompanyProfile


# def index(request):
#     """ A view to return the index page """
#     profiles = UserProfile.objects.all()
#     companies = CompanyProfile.objects.all()

#     context = {
#         'profile': profile,
#     }

#     return render(request, template, context)


# def index(request):
#     """ A view to return the index page """
#     profiles = UserProfile.objects.all()
#     companies = CompanyProfile.objects.all()

#     for p in profiles:
#         if p.user == request.user:
#             profile = p
#             if profile != p:
#                 for c in companies:
#                     if c.user == request.user:
#                         profile = c
#         else:
#             profile = ''

    
#     template = 'home/index.html'        

#     context = {
#         'profile': profile,
#     }

#     return render(request, template, context)



# OLD CODE
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