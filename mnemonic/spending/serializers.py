from rest_framework import serializers
from .models import Transaction, Account


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('name', 'id', 'availableCash',)

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id','registeredTime', 'executedTime', 'success', 'cashAmount')

