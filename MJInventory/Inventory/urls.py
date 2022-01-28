from Inventory.serializers import CustomerSKUSerializer
from django.urls.resolvers import URLPattern
from rest_framework import routers
from .views import CustomerSKUViewSets, InventoryViewSets,CustomerViewSets ,index
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register('Inventory', InventoryViewSets)
router.register('customerSKU',CustomerSKUViewSets)
router.register('customer',CustomerViewSets)



#router.register('search',CustomerSKUViewSets)

# URLPattern=[
#     path('', views.index, name='index'),
# ]