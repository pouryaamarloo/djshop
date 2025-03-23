from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable

from djshop.apps.cataluge.models import Category
from djshop.apps.cataluge.serializers.admin import CreateCategoryAdminSerializer, CategoryTreeSerializer, \
    NodeCategoryTreeSerializer, ModificationTreeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CreateCategoryAdminSerializer

    def get_queryset(self):
        if self.action == 'list':
            return Category.objects.filter(depth=1)
        else:
            return Category.objects.all()

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return CategoryTreeSerializer
            case 'create':
                return CreateCategoryAdminSerializer
            case 'retrieve':
                return NodeCategoryTreeSerializer

            case 'update':
                return ModificationTreeSerializer
            case 'partial_update':
                return ModificationTreeSerializer
            case 'destroy':
                return ModificationTreeSerializer

            case _:
                raise NotAcceptable


