from rest_framework.routers import SimpleRouter

from djshop.apps.cataluge.views.front import CategoryViewSet

router=SimpleRouter()
router.register('category',CategoryViewSet)
urlpatterns = [


] + router.urls