from rest_framework import viewsets

from djshop.apps.cataluge.models import Category
from djshop.apps.cataluge.serializers.admin import CreateCategoryAdminSerializer, CategoryTreeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CreateCategoryAdminSerializer

    def get_queryset(self):
        if self.action == 'list':
            return Category.objects.filter(depth=1)
        else:
            return Category.objects.all()



