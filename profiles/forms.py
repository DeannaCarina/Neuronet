from django import forms
from .models import UserProfile, CompanyProfile


class Profile(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('full_name', 'email', 'country',
                  'town_or_city', 'about_me', 'occupation',
                  'education_1', 'education_2', 'education_3',
                  'social_link_1', 'social_type_1', 'social_link_2',
                  'social_type_2', 'social_link_3', 'social_type_3',
                  'social_link_4', 'social_type_4', 'job_1',
                  'company_1', 'time_at_employer_1', 'job_2',
                  'company_2', 'time_at_employer_2', 'job_3',
                  'company_3', 'time_at_employer_3', 'image', 'video',
                  'strengths', 'weakness')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'country': 'Country',
            'town_or_city': 'Town or City',
            'about_me': 'About Me',
            'occupation': 'Occupation',
            'education_1': 'Education',
            'education_2': 'Education',
            'education_3': 'Education',
            'social_link_1': 'Link',
            'social_link_2': 'Link',
            'social_link_3': 'Link',
            'social_link_4': 'Link',
            'social_type_1': 'Social Media',
            'social_type_2': 'Social Media',
            'social_type_3': 'Social Media',
            'social_type_4': 'Social Media',
            'job_1': 'Job',
            'company_1': 'Company',
            'time_at_employer_1': 'Length of Employment',
            'job_2': 'Job',
            'company_2': 'Company',
            'time_at_employer_2': 'Length of Employment',
            'job_3': 'Job',
            'company_3': 'Company',
            'time_at_employer_3': 'Length of Employment',
            'image': 'Image',
            'video': 'Video',
            'strengths': 'Strengths',
            'weakness': 'Weaknesses'
        }

        for field in self.fields:
            placeholder = placeholders[field]
            # Start cursor on full_name field
            self.fields['full_name'].widget.attrs['autofocus'] = True
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


class Company(forms.ModelForm):

    class Meta:
        model = CompanyProfile
        fields = ('company_name', 'email', 'country',
                  'town_or_city', 'company_description', 'social_type_1',
                  'social_link_1', 'social_type_2', 'social_link_2',
                  'social_type_3', 'social_link_3', 'social_type_4',
                  'social_link_4', 'image', 'video')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'company_name': 'Company Name',
            'email': 'Contact Email',
            'country': 'Country',
            'town_or_city': 'Town or City',
            'company_description': 'Company Description',
            'social_link_1': 'Link',
            'social_link_2': 'Link',
            'social_link_3': 'Link',
            'social_link_4': 'Link',
            'social_type_1': 'Social Media',
            'social_type_2': 'Social Media',
            'social_type_3': 'Social Media',
            'social_type_4': 'Social Media',
            'image': 'Image',
            'video': 'Video'
        }

        for field in self.fields:
            placeholder = placeholders[field]
            # Start cursor on full_name field
            self.fields['company_name'].widget.attrs['autofocus'] = True
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
