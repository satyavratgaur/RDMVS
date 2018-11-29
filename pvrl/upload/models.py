from django.db import models

# Create your models here.

class Uploads(models.Model):
    up = models.FileField()
