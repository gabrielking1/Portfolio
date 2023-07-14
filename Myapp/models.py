from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import validate_email
# Create your models here.
class Feedback(models.Model):
    fullname = models.CharField(("fullname"), max_length=50)
    email = models.EmailField(("email"), max_length=254,validators=[validate_email])
    phone = PhoneNumberField()
    country = CountryField(blank=True, null=True)  
    # product = models.ForeignKey(Product,on_delete=models.CASCADE)
    feedback  = models.TextField(max_length=500)
    date = models.DateField(auto_now=True)
 
    @property
    def flag(self):
        return self.country.flag