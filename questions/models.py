from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField("created at")


# Create your models here.
