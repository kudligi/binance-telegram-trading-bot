from django.db import models
from django_fsm import FSMField, transition

# Create your models here.
class Bot(models.Model):
    WAITING_TO_BUY = "waiting2buy"
    WAITING_TO_SELL = "waiting2sell"
    STATUS_CHOICES = (
    (WAITING_TO_BUY , "waiting2buy")
    (WAITING_TO_SELL , "waiting2sell")
    )

    id = models.AutoField(primary_key=True)
    bot_name = models.CharField(max_length=100,unique=True,null=False, blank=False)
    state = FSMField(choices=STATUS_CHOICES,default=WAITING_TO_BUY)