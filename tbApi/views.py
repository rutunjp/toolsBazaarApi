from django.shortcuts import render

from rest_framework import viewsets

from .serializers import ListingSerializer
from .models import Listing


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all().order_by('title')
    serializer_class = ListingSerializer
