from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import CharField

# Create your models here.
class Customer(models.Model):
    CustomerName=models.CharField(max_length=100)
    CartID=models.CharField(max_length=20,null=True, blank=True)
    Platform=CharField(max_length=20,null=True, blank=True)
    Address=CharField(max_length=100,null=True, blank=True)
    Address2=CharField(max_length=100,null=True, blank=True)
    City=CharField(max_length=100,null=True, blank=True)
    State=CharField(max_length=20,null=True, blank=True)
    Zip=CharField(max_length=20,null=True, blank=True)
    Phone=CharField(max_length=30,null=True, blank=True)
    def __str__(self) -> str:
        return super().__str__()   

class Inventory(models.Model):
    LocalSku=models.CharField(max_length=100,primary_key = True)
    UPC=models.CharField(max_length=100, null=True, blank=True)
    QualityOnHold=models.IntegerField( default=0)
    ItemName=models.CharField(max_length=300)
    Warehouse=models.CharField(max_length=100, null=True, blank=True)
    Weight=models.FloatField(default=0, null=True, blank=True)
    heigh=models.FloatField(default=0, null=True, blank=True)
    width=models.FloatField(default=0, null=True, blank=True)
    depth=models.FloatField(default=0, null=True, blank=True)
    Category=models.CharField(max_length=100, null=True, blank=True)
    Avaliable=models.BooleanField(default=True)
    Discontinue=models.BooleanField(default=False)
    UpdateTime=models.DateTimeField(auto_now_add=True)
    UpdateBy=models.CharField(max_length=100, null=True, blank=True)


class CustomerSKU(models.Model):
    Customer=models.ForeignKey(Customer,on_delete=DO_NOTHING)
    Inventory=models.ForeignKey(Inventory,on_delete=DO_NOTHING)
    MerchantSku=CharField(max_length=100,null=True, blank=True)
    ManuallyFeedQty=models.IntegerField( default=999999)
    LastFeedTime=models.DateTimeField(auto_now_add=True)
    Remark=CharField(max_length=100,null=True, blank=True)
    def __str__(self) -> str:
        return super().__str__()
    
         
