from django.db import models
from djrichtextfield.models import RichTextField
# Create your models here.


class Post(models.Model):
    content = RichTextField()
    