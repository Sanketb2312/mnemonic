from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import TransactionSerializer, AccountSerializer
from .models import Transaction, Account

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

