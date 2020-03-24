from django.db import models
from cusers.models import CustomUser

# Create your models here.
class Receipts(models.Model):
    # NICK NAME should be unique
      
    user = models.IntegerField() #models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    paymentReference = models.CharField(max_length = 250, default="foobar")
    processorId = models.CharField(max_length = 250, default="foobar")
    transactionId = models.CharField(max_length=100, default="foobar")
    message = models.CharField(max_length=100, default="foobar")
    amount = models.CharField(max_length = 250, default="foobar")
    datetime = models.DateTimeField(auto_now=True)


    @classmethod
    def create(cls, user, paymentReference, processorId, transactionId, message, amount):
        receipt = cls(user=user, paymentReference=paymentReference, processorId= processorId,
        transactionId=transactionId, message=message, amount=amount)
        # do something with the book
        return receipt