from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse

# Create your models here.
class blog(models.Model):
    
    img=models.ImageField(upload_to="pics")
    content=models.TextField()
    datetime=models.DateTimeField(blank=True)
    thumbnail=models.ImageField(upload_to="pics")
    urllink=models.TextField(default="",blank=True)
    subheading1=models.TextField(default="",blank=True)
    para1=models.TextField(default="",blank=True)
    subheading2=models.TextField(default="",blank=True)
    para2=models.TextField(default="",blank=True)
    subheading3=models.TextField(default="",blank=True)
    para3=models.TextField(default="",blank=True)
    subheading4=models.TextField(default="",blank=True)
    para4=models.TextField(default="",blank=True)
    subheading5=models.TextField(default="",blank=True)
    para5=models.TextField(default="",blank=True)

    def __str__(self):
        return f"{self.content}"

    

class blogcomments(models.Model):
    sno=models.AutoField(primary_key=True)
    comment= models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog=models.ForeignKey(blog,related_name="comments",on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.comment,self.user}"
    