from django.db import models

# Create your models here.

class Add(models.Model):
    guest_say = models.TextField(max_length=500)
    guest_name = models.CharField(max_length=50,null = True)