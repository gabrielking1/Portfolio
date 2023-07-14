# Generated by Django 4.0 on 2023-05-10 09:19

from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, verbose_name='fullname')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('feedback', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
