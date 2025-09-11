from django.db import models

from django import forms

from django.utils import timezone

from django.contrib.auth.models  import User

from django.core.exceptions import ValidationError

class Dashboard(models.Model):

    Filetype = models.CharField(choices=[('image','image'),('videos','videos'),('files','files'),('gif','gif'),('link','link')],max_length=100)

    Uploaded_date = models.DateTimeField(default=timezone.now)

    User_id = models.ForeignKey(User,on_delete=models.CASCADE)

    File = models.FileField(upload_to='uploads/',null=True,blank=True)

    link = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.Filetype
    

    def clean(self):
        
        if self.File and self.link:
            
            raise forms.ValidationError("Please provide either a video file or a video link, not both.")

class Announcements(models.Model):

    title = models.CharField(max_length=100)

    message = models.TextField(max_length=100)

    uploaded_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

        
    