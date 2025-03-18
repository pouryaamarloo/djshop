from django.db import models
from treebeard.mp_tree import MP_Node


class Category(MP_Node):
    title=models.CharField(max_length=100,db_index=True)
    description=models.CharField(max_length=500,)
    is_public=models.BooleanField(default=True)
    slug=models.SlugField()


    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"







# Create your models here.
