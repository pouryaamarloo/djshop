
from django.urls import path
from rest_framework.routers import SimpleRouter

from djshop.apps.cataluge.views.admin import CategoryViewSet

router=SimpleRouter()
router.register('category',CategoryViewSet,basename='category')
urlpatterns = [

] + router.urls