from django.db import models
from treebeard.mp_tree import MP_Node

from djshop.apps.cataluge.managers import CategoryQuerySet


class Category(MP_Node):
    title=models.CharField(max_length=100,db_index=True)
    description=models.CharField(max_length=500,)
    is_public=models.BooleanField(default=True)
    slug=models.SlugField(allow_unicode=True)

    objects = CategoryQuerySet.as_manager()

    def __str__(self):
        return (f'{self.title} ({self.slug} , {self.is_public})')


    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"



class OptionGroup(models.Model):
    title=models.CharField(max_length=100,)



    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Option Group"
        verbose_name_plural = "Option Groups"
class OptionValue(models.Model):
    title=models.CharField(max_length=100,)
    group=models.ForeignKey(OptionGroup,on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Option Value"
        verbose_name_plural = "Option Values"


class ProductClass(models.Model):
    title=models.CharField(max_length=100,db_index=True)
    description=models.CharField(max_length=500,)
    slug=models.SlugField(unique=True,allow_unicode=True)

    track_stock=models.BooleanField(default=True)
    shipping=models.BooleanField(default=True)
    options=models.ManyToManyField('Option',blank=True)

    def has_attributes(self):
        return self.attributes.exists()


    def __str__(self):
        return f"{self.title},{self.options},{self.track_stock},{self.shipping}"


    class Meta:
        verbose_name = "Product Class"
        verbose_name_plural = "Product Classes"

class ProductAttribute(models.Model):

    class ProductAttributeTypes(models.TextChoices):
        text = "text"
        integer = "integer"
        float = "float"
        option= "option"
        multi_option= "multi_option"
    product_class=models.ForeignKey(ProductClass,on_delete=models.CASCADE,related_name='attributes')
    option_group=models.ForeignKey(OptionGroup,on_delete=models.PROTECT,related_name='options_groups')
    title=models.CharField(max_length=100)
    type=models.CharField(max_length=100,choices=ProductAttributeTypes.choices,default=ProductAttributeTypes.text)
    required=models.BooleanField(default=True)
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "product attribute"
        verbose_name_plural = "product attributes"

class Option(models.Model):
    class OptionTypes(models.TextChoices):
        text = "text"
        integer = "integer"
        float = "float"
        option= "option"
        multi_option= "multi_option"
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    type=models.CharField(max_length=100,choices=OptionTypes.choices,default=OptionTypes.text)
    group=models.ForeignKey(OptionGroup,on_delete=models.PROTECT,related_name='options')


class Product(models.Model):
    class ProductTypes(models.TextChoices):
        standalone = "standalone"
        parent='parent'
        child='child'
    structure=models.CharField(max_length=16,choices=ProductTypes.choices,default=ProductTypes.standalone)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=100)
    upc=models.CharField(max_length=10)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"





# Create your models here.
