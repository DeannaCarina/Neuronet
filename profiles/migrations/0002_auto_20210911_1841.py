# Generated by Django 3.2.7 on 2021-09-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='social_type_1',
            field=models.CharField(blank=True, default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='social_type_2',
            field=models.CharField(blank=True, default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='social_type_3',
            field=models.CharField(blank=True, default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='social_type_4',
            field=models.CharField(blank=True, default='N/A', max_length=100),
        ),
    ]