from django.db import models
from django.contrib.auth.models import User 

class Blogs(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    date_posted=models.DateField(auto_now_add=True)
    blog_image=models.ImageField(upload_to='blog-image/',blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title[: 50]

