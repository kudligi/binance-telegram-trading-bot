from django.db import models

# Create your models here.
class User(models.Model):
    chat_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=25)
    knows = models.BooleanField()
