# Generated by Django 3.2.7 on 2021-09-12 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_auto_20210911_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('town_or_city', models.CharField(blank=True, max_length=40)),
                ('company_description', models.TextField(blank=True, default='N/A', max_length=999)),
                ('image_url', models.URLField(blank=True, max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('video', models.TextField(blank=True, default='N/A', max_length=999)),
                ('social_type_1', models.CharField(blank=True, default='N/A', max_length=100)),
                ('social_link_1', models.TextField(blank=True, default='N/A', max_length=999)),
                ('social_type_2', models.CharField(blank=True, default='N/A', max_length=100)),
                ('social_link_2', models.TextField(blank=True, default='N/A', max_length=999)),
                ('social_type_3', models.CharField(blank=True, default='N/A', max_length=100)),
                ('social_link_3', models.TextField(blank=True, default='N/A', max_length=999)),
                ('social_type_4', models.CharField(blank=True, default='N/A', max_length=100)),
                ('social_link_4', models.TextField(blank=True, default='N/A', max_length=999)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]