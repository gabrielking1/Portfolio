from django import forms
from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.bootstrap import Accordion, AccordionGroup

from phonenumber_field.formfields import PhoneNumberField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column,Field, Button
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from django.forms.widgets import Select
from django.utils.html import format_html
from django_countries import countries
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Feedback




class FeedbackForm(forms.ModelForm):
    phone = PhoneNumberField(
        widget=PhoneNumberInternationalFallbackWidget(attrs={
            'placeholder': 'Enter valid Phone number',
            'class': 'form-control'
        }),
        
    )
    country = CountryField(blank_label='Select country').formfield(widget=CountrySelectWidget(attrs={'class': 'form-control'}))
    # country = CountryField(widget=CountryFlagSelectWidget())
    # country = CountryField(blank_label='Select country')
    # .formfield(widget=CountrySelectWidget(attrs={
    #     'class': 'custom-select d-block w-100',
    # }))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter valid Email'}))
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError('Enter a valid email address(e.g. Example@hello.com')
        return email
    fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your full name ,'}), label="First name and Last name ")
    feedback = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'i need your service ,','rows':4, 'cols':15}),
    label="Enter Your Request",
    )
    class Meta:
        model = Feedback
        fields = "__all__"
        
        
    
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        # self.fields['country'].widget.choices = [('', 'select country ')] + list(self.fields['country'].widget.choices)[1:]
        self.helper = FormHelper()
        self.helper.layout = Layout(
            
             Accordion(
                AccordionGroup('Contact Details',
        Row(
                Column('email', css_class='form-group col-md-6 mb-0',style='background-color: #f0f0f0'),
                Column('fullname', css_class='form-group col-md-6 mb-0',style='background-color: #f0f0f0'),
                css_class='form-row',style='color: black',
            ),
            Row(
                Column('country', css_class='form-group col-md-3 mb-0',style='background-color: #f0f0f0'),
                Column('phone', css_class='form-group col-md-9 mb-0',style='background-color: #f0f0f0'),
                css_class='form-row',style='color: black',
            ),
    ),
    AccordionGroup('Message', Field('feedback', css_class="extra",style='color: black',)
    ),flush=True,
        always_open=True,
                
            ),
            Submit('submit', 'Send',css_class="btn-primary"),
            Button('cancel', 'Cancel',css_class="btn-secondary")
            
        )
        
