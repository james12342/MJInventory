from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import InventorySerializer
from rest_framework import viewsets
from rest_framework.response import Response
from .models import CustomerSKU, Inventory

class InventoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Inventory.objects.all()
        serializer = InventorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Inventory.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = InventorySerializer(user)
        return Response(serializer.data)