from django.db import models
from django_fsm import FSMField, transition

# Create your models here.
class LimitOrder(models.Model):
    STATUS_CREATED = 'created'
    STATUS_FILLED = 'filled'
    STATUS_PARTIALLY_FILLED = 'partially_filled'
    STATUS_CANCELLED = 'cancelled'
    STATUS_CHOICES = (
        (STATUS_CREATED, 'created'),
        (STATUS_FILLED, 'filled'),
        (STATUS_CANCELLED, 'cancelled'),
        (STATUS_PARTIALLY_FILLED, 'partially_filled'),
        )
    TYPE_CHOICES = [
        ("BUY", "BUY"),
        ("SELL", "SELL")
    ]
    id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=100,unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=10,null=False, blank=False)
    amount = models.DecimalField(max_digits=20, decimal_places=10, default=0)
    quantity = models.DecimalField(max_digits=20, decimal_places=10,null=False, blank=False)
    filled_quantity = models.DecimalField(max_digits=20, decimal_places=10, default=0)
    symbol = models.CharField(max_length=10,null=False, blank=False)
    side = models.CharField(max_length=5,choices=TYPE_CHOICES,null=False, blank=False)
    status = FSMField(choices=STATUS_CHOICES,default=STATUS_CREATED)
    
    @transition(field=status, source=STATUS_CREATED, target=STATUS_FILLED)
    def fill(self):
        self.filled_quantity = self.quantity
        self.amount = self.price * self.filled_quantity
        print("Order ID:{} FILLED".format(self.id))

    @transition(field=status, source=STATUS_CREATED, target=STATUS_CANCELLED)
    def cancel(self):
        print("Order ID:{} CANCELLED".format(self.id))

    @transition(field=status, source=[STATUS_CREATED, STATUS_PARTIALLY_FILLED], target=STATUS_PARTIALLY_FILLED)
    def partially_fill(self, qty):
        self.filled_quantity = qty
        self.amount = self.price * self.filled_quantity
        print("Order ID:{} PARTIALLY FILLED".format(self.id))

    def Display(self):
        print("---------------------------------------------")
        print("internal ID:{} Order ID:{} STATUS:{}".format(self.id, self.order_id, self.status))
        print("Symbol:{} Side:{}".format(self.symbol, self.side))
        print("PRICE:{} QUANTITY:{}".format(self.price, self.quantity))
        print("Filled Quantity:{} Amount:{}".format(self.filled_quantity, self.amount))
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")