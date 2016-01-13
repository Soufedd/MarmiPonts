from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Information(models.Model):
    user = models.ForeignKey(User)
    Last_name = models.CharField(max_length=15, null=True, blank=True)
    First_name = models.CharField(max_length=15, null=True, blank=True)
    Departement = models.CharField(max_length=15, null=True, blank=True)
    Room_number = models.CharField(max_length=5)
    Telephone_number = models.CharField(max_length=15, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.Last_name

