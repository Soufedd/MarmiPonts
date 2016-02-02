from django.db import models
from Core.models import Information
from django.forms import ModelForm



# Create your models here.
class Forum(models.Model):  
    title = models.CharField(max_length=60)
    def __unicode__(self):
        return self.title

class Thread(models.Model):
    id_name= models.ForeignKey(Information)
    forum = models.ForeignKey(Forum)
    title = models.CharField(max_length=60)
    content = models.TextField(max_length=10000)    
    pub_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title

class Post(models.Model):
    thread = models.ForeignKey(Thread)
    content = models.TextField(max_length=10000)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title

