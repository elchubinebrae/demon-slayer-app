from django import forms
from django.forms import ModelForm
from .models import DemonSlayer, ContactUsNow

class AddDemonSlayer(ModelForm):
    class Meta:
        model = DemonSlayer
        fields = ("first_name", "last_name", "age", "element_type", "category")

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.TextInput(attrs={"class": "form-control"}),
            "element_type": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.TextInput(attrs={"class": "form-control"})
        }

class ContactForm(ModelForm):
    class Meta:
        model = ContactUsNow
        fields = ("first_name", "last_name", "email_address", "enquiry")

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name" : forms.TextInput(attrs={"class": "form-control"}),
            "email_address": forms.EmailInput(attrs={"class": "form-control"}),
            "enquiry": forms.TextInput(attrs={"class": "form-control"})
        }