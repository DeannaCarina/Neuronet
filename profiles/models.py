from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """ Model to hold all user profile information """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=True, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True, default='')
    about_me = models.TextField(max_length=999, blank=True, default='')
    occupation = models.CharField(max_length=100, null=False, blank=False)
    education_1 = models.CharField(max_length=100, blank=True, default='')
    education_2 = models.CharField(max_length=100, blank=True, default='')
    education_3 = models.CharField(max_length=100, blank=True, default='')
    social_type_1 = models.CharField(max_length=100, blank=True, default='')
    social_link_1 = models.URLField(max_length=999, blank=True, default='')
    social_type_2 = models.CharField(max_length=100, blank=True, default='')
    social_link_2 = models.URLField(max_length=999, blank=True, default='')
    social_type_3 = models.CharField(max_length=100, blank=True, default='')
    social_link_3 = models.URLField(max_length=999, blank=True, default='')
    social_type_4 = models.CharField(max_length=100, blank=True, default='')
    social_link_4 = models.URLField(max_length=999, blank=True, default='')
    job_1 = models.CharField(max_length=100, blank=True, default='')
    company_1 = models.CharField(max_length=100, blank=True, default='')
    time_at_employer_1 = models.CharField(
        max_length=100, blank=True, default='')
    job_2 = models.CharField(max_length=100, blank=True, default='')
    company_2 = models.CharField(max_length=100, blank=True, default='')
    time_at_employer_2 = models.CharField(
        max_length=100, blank=True, default='')
    job_3 = models.CharField(max_length=100, blank=True, default='')
    company_3 = models.CharField(
        max_length=100, blank=True, default='')
    time_at_employer_3 = models.CharField(
        max_length=100, blank=True, default='')
    image_url = models.URLField(max_length=1000, blank=True, default='')
    image = models.ImageField(null=True, blank=True)
    video = models.URLField(max_length=999, blank=True, default='')
    strengths = models.CharField(max_length=100, blank=True, default='')
    weakness = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.full_name


class CompanyProfile(models.Model):
    """ Model to hold basic company information """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=True, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True, default='')
    company_description = models.TextField(
        max_length=999, blank=True, default='')
    image_url = models.URLField(max_length=1000, blank=True, default='')
    image = models.ImageField(null=True, blank=True)
    video = models.URLField(max_length=999, blank=True, default='')
    social_type_1 = models.CharField(max_length=100, blank=True, default='')
    social_link_1 = models.URLField(max_length=999, blank=True, default='')
    social_type_2 = models.CharField(max_length=100, blank=True, default='')
    social_link_2 = models.URLField(max_length=999, blank=True, default='')
    social_type_3 = models.CharField(max_length=100, blank=True, default='')
    social_link_3 = models.URLField(max_length=999, blank=True, default='')
    social_type_4 = models.CharField(max_length=100, blank=True, default='')
    social_link_4 = models.URLField(max_length=999, blank=True, default='')

    def __str__(self):
        return self.company_name
