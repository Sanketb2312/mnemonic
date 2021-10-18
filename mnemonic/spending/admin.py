from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Transaction, Account

admin.site.register(Account)
admin.site.register(Transaction)
