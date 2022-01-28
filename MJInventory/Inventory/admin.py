from django.contrib import admin
from .models import CustomerSKU, Inventory,Customer

# Register your models here.

admin.site.register(Inventory)
admin.site.register(CustomerSKU)
admin.site.register(Customer)

