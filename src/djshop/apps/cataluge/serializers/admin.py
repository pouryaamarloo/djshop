from drf_spectacular.utils import extend_schema_serializer, extend_schema_field
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from djshop.apps.cataluge.models import Category


class CreateCategoryAdminSerializer(serializers.ModelSerializer):
    parent = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        parent=validated_data.pop('parent',None)

        if parent is None:
            instance=Category.add_root(**validated_data)
        else :
            parent_node=get_object_or_404(Category,pk=parent)
            instance=parent_node.add_child(parent=parent, **validated_data)

        return instance
    class Meta:
        model = Category
        fields = ('id','title','slug','is_public','parent')


class CategoryTreeSerializer(serializers.ModelSerializer):
        children = serializers.SerializerMethodField()


        def get_children(self,obj):
            return CategoryTreeSerializer(obj.get_children(),many=True).data



        class Meta:
            model = Category
            fields = ('id','title','slug','is_public','children')

CategoryTreeSerializer.get_children=extend_schema_field(serializers.ListField(child=CategoryTreeSerializer()))(CategoryTreeSerializer.get_children)

class NodeCategoryTreeSerializer(serializers.ModelSerializer):


    class Meta:
        model=Category
        fields='__all__'

class ModificationTreeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields=fields = ('id','title','is_public',)
