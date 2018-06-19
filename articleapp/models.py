from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    author= models.CharField(max_length=200,null=True,blank=True)
    vote = models.PositiveIntegerField(default=0,null=True,blank=True)
	

