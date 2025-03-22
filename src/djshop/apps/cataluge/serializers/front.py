from djshop.apps.cataluge import serializers
from djshop.apps.cataluge.models import Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
