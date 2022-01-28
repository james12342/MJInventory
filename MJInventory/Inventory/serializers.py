from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import CustomerSKU, Inventory,Customer


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        # fields = '__all__'
        #  class Meta:
       
        fields = ['LocalSku', 'UPC', 'QualityOnHold',
                  'ItemName', 'Warehouse', 'Weight', 'heigh', 'width', 'depth', 'Category','Avaliable','Discontinue','UpdateTime','UpdateBy']


class CustomerSKUSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerSKU
        fields='__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'


        

