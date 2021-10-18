from django.db import models
from datetime import *
import django.utils.timezone

# Create your models here.

class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    availableCash = models.DecimalField(decimal_places=3, max_digits=15)

    def __init__(self, id, name, availableCash):
        self.name = name
        self.id = id
        self.availableCash = availableCash

    def getCash(self):
        return self.availableCash



class Transaction(models.Model):

    id = models.IntegerField(primary_key=True)
    registeredTime = models.DateTimeField(default=django.utils.timezone.now())
    executedTime = models.DateTimeField(default=django.utils.timezone.now())
    success = models.BooleanField(default=False)
    cashAmount = models.DecimalField(default=0, decimal_places=3, max_digits=15)
    sourceAccount = Account(id=1, name="Olav", availableCash="500")
    destinationAccount = Account(id=1, name="Olav", availableCash="500")

    def transferMoney(self, sourceAccount : Account, destinationAccount : Account, amount):
        self.checkLegalTransaction(amount, sourceAccount)
        sourceAccount.availableCash-=amount
        destinationAccount.availableCash+=amount

    def checkLegalTransaction(self, amount, account : Account):
        if amount < 0:
            raise IndentationError("Negative amount is not aloud")
        if account.availableCash < amount:
            raise IndentationError("You dont have enough money on your account for this transaction")




