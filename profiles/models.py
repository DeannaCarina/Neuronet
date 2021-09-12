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
    town_or_city = models.CharField(max_length=40, blank=True)
    about_me = models.TextField(max_length=999, blank=True, default="N/A")
    occupation = models.CharField(max_length=100, null=False, blank=False)
    education_1 = models.CharField(max_length=100, blank=True, default="N/A")
    education_2 = models.CharField(max_length=100, blank=True, default="N/A")
    education_3 = models.CharField(max_length=100, blank=True, default="N/A")
    social_type_1 = models.CharField(max_length=100, blank=True, default="N/A")
    social_link_1 = models.TextField(max_length=999, blank=True, default="N/A")
    social_type_2 = models.CharField(max_length=100, blank=True, default="N/A")
    social_link_2 = models.TextField(max_length=999, blank=True, default="N/A")
    social_type_3 = models.CharField(max_length=100, blank=True, default="N/A")
    social_link_3 = models.TextField(max_length=999, blank=True, default="N/A")
    social_type_4 = models.CharField(max_length=100, blank=True, default="N/A")
    social_link_4 = models.TextField(max_length=999, blank=True, default="N/A")
    job_1 = models.CharField(max_length=100, blank=True, default="N/A")
    company_1 = models.CharField(max_length=100, blank=True, default="N/A")
    time_at_employer_1 = models.CharField(
        max_length=100, blank=True, default="N/A")
    job_2 = models.CharField(max_length=100, blank=True, default="N/A")
    company_2 = models.CharField(max_length=100, blank=True, default="N/A")
    time_at_employer_2 = models.CharField(
        max_length=100, blank=True, default="N/A")
    job_3 = models.CharField(max_length=100, blank=True, default="N/A")
    company_3 = models.CharField(
        max_length=100, blank=True, default="N/A")
    time_at_employer_3 = models.CharField(
        max_length=100, blank=True, default="N/A")
    image_url = models.URLField(max_length=1000, blank=True)
    image = models.ImageField(null=True, blank=True)
    video = models.TextField(max_length=999, blank=True, default="N/A")
    strengths = models.CharField(max_length=100, blank=True, default="N/A")
    weakness = models.CharField(max_length=100, blank=True, default="N/A")

    def __str__(self):
        return self.full_name


class CompanyProfile(models.Model):
    """ Model to hold basic company information """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=True, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    company_description = models.TextField(
        max_length=999, blank=True, default="N/A")
    image_url = models.URLField(max_length=1000, blank=True)
    image = models.ImageField(null=True, blank=True)
    video = models.TextField(max_length=999, blank=True, default="N/A")
    social_type_1 = models.CharField(max_length=100, blank=True, default="N/A")
    social_link_1 = models.TextField(max_length=999, blank=True, default="N/A")
    social_type_2 = models.CharField(max_length=100, blank=True, default="N/A")
    social_link_2 = models.TextField(max_length=999, blank=True, default="N/A")
    social_type_3 = models.CharField(max_length=100, blank=True, default="N/A")
    social_link_3 = models.TextField(max_length=999, blank=True, default="N/A")
    social_type_4 = models.CharField(max_length=100, blank=True, default="N/A")
    social_link_4 = models.TextField(max_length=999, blank=True, default="N/A")

    def __str__(self):
        return self.company_name
