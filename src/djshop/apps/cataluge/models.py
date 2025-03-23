from django.db import models
from treebeard.mp_tree import MP_Node

from djshop.apps.cataluge.managers import CategoryQuerySet


class Category(MP_Node):
    title=models.CharField(max_length=100,db_index=True)
    description=models.CharField(max_length=500,)
    is_public=models.BooleanField(default=True)
    slug=models.SlugField()

    objects = CategoryQuerySet.as_manager()

    def __str__(self):
        return (f'{self.title} ({self.slug} , {self.is_public})')


    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"







# Create your models here.
