from django.contrib import admin
from myapp.models import Transaction

@admin.register(Transaction)
class Transaction_admin(admin.ModelAdmin):
    list_display=['uuid','expance_name','amount','category']

