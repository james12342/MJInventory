from django.db import reset_queries
from django.http.response import JsonResponse
from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest,HttpResponse
from .models import Customer, Inventory,CustomerSKU
from rest_framework.viewsets import ModelViewSet
from .serializers import CustomerSKUSerializer, InventorySerializer,CustomerSerializer
from django.db.models import Q
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import UserRateThrottle
from datetime import datetime
import json
# from django_filters.rest_framework import DjangoFilterBackend

###############  Inventory ####################
# Create your views here.
class InventoryAPIView(APIView):
    serializer_class = InventorySerializer
    throttle_scope = "invs_app"

    def get_queryset(self):
        invs = Inventory.objects.all()
        return invs

    def get(self, request, *args, **kwargs):

        print("##### get request detected #####")
        try:
            LocalSku_value = request.query_params["LocalSku"]
            if LocalSku_value != None:
                print("getting LocalSku:",LocalSku_value)
                inv = Inventory.objects.get(LocalSku=LocalSku_value)
                serializer = InventorySerializer(inv)
                print("serializer:",serializer)
        except:
            print("##### get all queryset #####")
            invs = self.get_queryset()
            serializer = InventorySerializer(invs, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        inv_data = request.data
        print (inv_data)
        new_inv = Inventory.objects.create(
            LocalSku=inv_data["LocalSku"], 
            UPC=inv_data["UPC"], 
            QualityOnHold=inv_data["QualityOnHold"], 
            ItemName=inv_data["ItemName"], 
            Warehouse=inv_data["Warehouse"], 
            Weight=inv_data["Weight"],
            heigh=inv_data["heigh"],
            width=inv_data["width"],
            depth=inv_data["depth"],
            Avaliable=inv_data["Avaliable"],
            Discontinue=inv_data["Discontinue"]           
            )
       
        new_inv.save()

        serializer = InventorySerializer(new_inv)

        return Response(serializer.data)
   

    def put(self, request, *args, **kwargs):
        LocalSku_Value = request.query_params["LocalSku"]
        inv_object = Inventory.objects.get(LocalSku=LocalSku_Value)

        data = request.data
        print (data)
        inv_object.LocalSku = data["LocalSku"]
        if is_json_key_present(data,"UPC")==True:
            print ("upc present")
            inv_object.UPC = data["UPC"]
        if is_json_key_present(data,"QualityOnHold"):  
           inv_object.QualityOnHold = data["QualityOnHold"]
        if is_json_key_present(data,"ItemName"):  
           inv_object.ItemName = data["ItemName"]
        if is_json_key_present(data,"Warehouse"):  
           inv_object.Warehouse = data["Warehouse"]
        if is_json_key_present(data,"Weight"):  
           inv_object.Weight = data["Weight"]
        if is_json_key_present(data,"heigh"): 
           inv_object.heigh = data["heigh"]
        if is_json_key_present(data,"width"): 
           inv_object.width = data["width"]
        if is_json_key_present(data,"depth"): 
           inv_object.depth = data["depth"]
        if is_json_key_present(data,"Avaliable"): 
           inv_object.Avaliable = data["Avaliable"]
        if is_json_key_present(data,"Discontinue"): 
           inv_object.Discontinue = data["Discontinue"]
        if is_json_key_present(data,"UpdateTime"): 
           inv_object.UpdateTime = data["UpdateTime"]
        if is_json_key_present(data,"UpdateBy"): 
           inv_object.UpdateBy = data["UpdateBy"]
        inv_object.save()

        serializer = InventorySerializer(inv_object)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        LocalSku_Value = request.query_params["LocalSku"]
        inv_object = Inventory.objects.get(LocalSku=LocalSku_Value)
        data = request.data

        inv_object.LocalSku = data["LocalSku"]
        if is_json_key_present(data,"UPC")==True:
            print ("upc present")
            inv_object.UPC = data["UPC"]
        if is_json_key_present(data,"QualityOnHold"):  
           inv_object.QualityOnHold = data["QualityOnHold"]
        if is_json_key_present(data,"ItemName"):  
           inv_object.ItemName = data["ItemName"]
        if is_json_key_present(data,"Warehouse"):  
           inv_object.Warehouse = data["Warehouse"]
        if is_json_key_present(data,"Weight"):  
           inv_object.Weight = data["Weight"]
        if is_json_key_present(data,"heigh"): 
           inv_object.heigh = data["heigh"]
        if is_json_key_present(data,"width"): 
           inv_object.width = data["width"]
        if is_json_key_present(data,"depth"): 
           inv_object.depth = data["depth"]
        if is_json_key_present(data,"Avaliable"): 
           inv_object.Avaliable = data["Avaliable"]
        if is_json_key_present(data,"Discontinue"): 
           inv_object.Discontinue = data["Discontinue"]
        if is_json_key_present(data,"UpdateTime"): 
           inv_object.UpdateTime = data["UpdateTime"]
        if is_json_key_present(data,"UpdateBy"): 
           inv_object.UpdateBy = data["UpdateBy"]

        inv_object.save()
        serializer = InventorySerializer(inv_object)

        return Response(serializer.data)
    
    def delete(self, request, *args, **kwargs):
        LocalSku_Value = request.query_params["LocalSku"]
        inv_object = Inventory.objects.get(LocalSku=LocalSku_Value)      
        inv_object.delete()
        serializer = InventorySerializer(inv_object)
        return Response(serializer.data)

def search_product(request):
    """ search function  """
    if request.method == "POST":
        query_LocalSku = request.POST.get('LocalSku', None)
        print ("searching SKU:"+query_LocalSku)
        if query_LocalSku:
            results = Inventory.objects.filter(Q(LocalSku__contains=query_LocalSku) | Q(ItemName__contains=query_LocalSku) | Q(Warehouse__contains=query_LocalSku)| Q(Avaliable__contains=query_LocalSku))
            return render(request, 'index_Inventory.html', {"results":results})

    return render(request, 'Inventory/index.html')

def update_InventorySingleItem(request):
    
    sku=request.GET.get('sku')
    qty=request.GET.get('qty')

    print ("update inventory for sku:"+sku+" qty:"+qty)
    # LocalSku_Value = request.POST.get('LocalSku', None)
    # print ("LocalSku_Value:"+LocalSku_Value)
    inv_object = Inventory.objects.get(LocalSku=sku)

   # data = request.data
   # print (data)
    inv_object.QualityOnHold = qty
    inv_object.UpdateTime=datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f%z')
    inv_object.UpdateBy="Human"

   
    
    inv_object.save()
    print ("update inventory for sku:"+sku+"Qty:"+qty+" successfully")
    return render(request, 'Inventory/index.html')

def update_InventoryByExcel(request):
    
    print ("update inventory by excel jsondata NOW----->C")
    jsonData=request.GET.get('jsonData')
    print(jsonData)
    #Load JSON string into a dictionary
    json_data = json.loads(jsonData)
    json_length = len(json_data)
    for i in range(json_length):
       sku=json_data[i]['SKU']
       qty=json_data[i]['CustomerInventoryFeed']
       print(json_data[i]['SKU'])

    
   
     
       inv_object = Inventory.objects.get(LocalSku=sku)

   # data = request.data
   # print (data)
       inv_object.QualityOnHold = qty
       inv_object.UpdateTime=datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f%z')
       inv_object.UpdateBy="Human Batch"

   
    
       inv_object.save()
       print ("update inventory for sku:"+sku+"--Qty:"+qty+" successfully")
    return render(request, 'Inventory/index.html')
   
def update_InventoryByJson(request):
    jsonValue=request.GET.get('jsonValue')
    print ("update inventory from jsonvalue:"+jsonValue)
    # now update the inventory
    # change the JSON string into a JSON object
    jsonObject = json.loads(jsonValue)
    #print ("update inventory from jsonObject:"+jsonObject)
    # print the keys and values
    length = len(jsonObject)
    
    for i in range(0, length, 1):
      sku=jsonObject[i]['SKU']
      qty=jsonObject[i]['CustomerInventoryFeed']
      print ("SKU:"+sku+" Qty:"+qty)
      # now update the inventory
      inv_object = Inventory.objects.get(LocalSku=sku)

   # data = request.data
   # print (data)
      inv_object.QualityOnHold = qty
      inv_object.UpdateTime=datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f%z')
      inv_object.UpdateBy="Batch Update"
      inv_object.save()
      print ("update inventory for sku:"+sku+" successfully")
    return render(request, 'Inventory/index.html')

def index(request):
    return HttpResponse("Hello Majesticpet Inventory Index")

#Inventory Homepage
def InventoryHome(request):
    theInventory=Inventory.objects
    theItemcount = Inventory.objects.count()
   
    context = {
        'theInventory':theInventory,
        'theItemcount': theItemcount
    }
    print(context)
    if request.method == "GET":
      print('here request.method == "GET"')
      return render(request, 'index_Inventory.html',context)
    elif request.is_ajax():
      data = request.POST.get('Inventory', None)
      if data:
         response = { 'Inventory': data }
         return JsonResponse(response)
      else:
            response = { 'Inventory': "" }
      return JsonResponse(response)

#Inventory DetailPage
def InventoryDetails(request,inventory_id):
    inventorydetail=get_object_or_404(Inventory,pk=inventory_id)
    return render(request,
                  "Inventory/details.html",
                  {"inventorydetail": inventorydetail}
                  )

#InventoryViewSets
class InventoryViewSets(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


###############  CustomerSKU ####################
#CustomerSKU Homepage
def CustomerSKUHome(request):
    theCustomerSKU=CustomerSKU.objects
    context={'theCustomerSKU':theCustomerSKU}

    return render(
      request,
      'CustomerSKU.html',
      context
    )

#CustomerSKUViewSets
class CustomerSKUViewSets(ModelViewSet):
    queryset=CustomerSKU.objects.all()
    serializer_class=CustomerSKUSerializer

def search(request):
    query=None
    results=[]
    if request.method=="GET":
        query=request.GET.get('search')
        results=CustomerSKU.objects.filter(Q(CustomerName__icontains=query) )
    return  render(request,'index_Inventory.html',{'query': query,
                                          'results': results})

def FilterCustomerSKUView(request):
    qs=CustomerSKU.objects.all()
    print(qs.get(id=1))
    sku_contains_query=request.GET.get('SKU_contains')
   
    if sku_contains_query !='' and sku_contains_query is not None:
        print('filter for:',sku_contains_query)
        qs=qs.filter(CustomerName__contains=sku_contains_query)
        print('result is=============>' ,qs)
    context={
        'queryset':qs
    }
    print('Context------------------------->',context)
    return render(request,'index_Inventory.html',context)
# api All functions, get, post, put, patch
def is_json_key_present(json, key):
        try:
           buf = json[key]
        except KeyError:
           return False

        return True


###############  Customer ##########################
class CustomerViewSets(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

def CustomerSKUHome(request):

    theCustomerSKU=CustomerSKU.objects
    thecount = CustomerSKU.objects.count()
   
    theCustomer=Customer.objects
    print(theCustomer.all)
    context={'theCustomer':theCustomer,'theCustomerSKU':theCustomerSKU,'thecount':thecount}
    #print(context)
    return render(
      request,
      'CustomerSKU.html',
     
      context
    )

def AddOrUpdate_CustomerSKUByJson(request):
    jsonValue=request.GET.get('jsonValue')
    print ("Add or update CustomerSKU from jsonvalue:"+jsonValue)
    # now update the CustomerSKU
    # change the JSON string into a JSON object
    jsonObject = json.loads(jsonValue)
    
    # print the keys and values
    length = len(jsonObject)
    
    for i in range(0, length, 1):
      sku=jsonObject[i]['SKU']
      qty=jsonObject[i]['CustomerInventoryFeed']
      print ("SKU:"+sku+" Qty:"+qty)
      # now update the inventory
      inv_object = Inventory.objects.get(LocalSku=sku)

   # data = request.data
   # print (data)
      inv_object.QualityOnHold = qty
      inv_object.UpdateTime=datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f%z')
      inv_object.UpdateBy="Batch Update"
      inv_object.save()
      print ("update inventory for sku:"+sku+" successfully")
    return render(request, 'Inventory/index.html')