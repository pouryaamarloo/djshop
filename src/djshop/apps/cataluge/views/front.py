from rest_framework import viewsets

from djshop.apps.cataluge.models import Category
from djshop.apps.cataluge.serializers.front import CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class =CategorySerializer