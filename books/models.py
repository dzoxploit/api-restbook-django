from django.db import models
import uuid
# Create your models here.
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Book(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster_image = models.ImageField(upload_to=upload_to, blank=True, null=True)