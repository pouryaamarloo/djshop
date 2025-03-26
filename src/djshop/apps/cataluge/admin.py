from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.models import Count
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from . import models
from .models import Category, ProductClass, Option, OptionGroup


class CategoryAdmin(TreeAdmin):
    form=movenodeform_factory(Category)
    list_display = ['title','slug' ]


class ProductAttributeTabular(admin.TabularInline):
    model = models.ProductAttribute
    extra = 2

class AttributeCountFilter(admin.SimpleListFilter):
    title = 'Attribute Count'
    parameter_name = 'attr_count'

    def lookups(self, request, model_admin):
        return [("high","greater than 5"),
                 ("low","lower than 5")
        ]

    def queryset(self, request, queryset):
        attr_count=queryset.annotate(attribute_count=Count('attributes'))
        if self.value()=="high":
            return attr_count.filter(attribute_count__gt=5)
        elif self.value()=="low":
            return attr_count.filter(attribute_count__lte=5)
        else :
            return attr_count




@admin.register(ProductClass)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','slug','track_stock','shipping','attribute_count']
    list_filter = ['track_stock','shipping',AttributeCountFilter,]
    inlines = [ProductAttributeTabular]


    def attribute_count(self, obj):
        return obj.attributes.count()





class CrmAdmin(admin.AdminSite):
    site_title="Djshop"
    admin_site_name="Djshop"
    site_header = "Djshop"
# Register your models here.
admin.site.register(Option)
admin.site.register(Category, CategoryAdmin)
admin.site.register(OptionGroup)

