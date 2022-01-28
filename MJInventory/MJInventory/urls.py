"""PowerInventoryProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path,include

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from Inventory.serializers import InventorySerializer
from Inventory.urls import router
from Inventory.urls import index
from Inventory import views as InventoryView
from django.conf.urls.static import static
from django.conf import Settings, settings




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('Inventory/',include('Inventory.urls')),
    path('inventory', InventoryView.InventoryHome, name='InventoryHome'),
    path('customersku/', InventoryView.CustomerSKUHome, name='CustomerSKUHome'),
    path('filter/', InventoryView.FilterCustomerSKUView, name='bootstrap'),
    path('search/', InventoryView.search_product,name='search'),
    path('ajaxUpdateInventory/', InventoryView.update_InventorySingleItem,name='ajaxUpdateInventory'),
    path('ajaxUpdateInventory_Byjson/', InventoryView.update_InventoryByJson,name='ajaxUpdateInventory_Byjson'),
    path('apis/', InventoryView.InventoryAPIView.as_view()),
    path('api/', include(router.urls)),
    path('Inventory_ajax/', InventoryView.InventoryHome, name = "InventoryHome_ajax"),
    path('UpdateInventoryByExcel/', InventoryView.update_InventoryByExcel,name='UpdateInventoryByExcel'),
   


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
