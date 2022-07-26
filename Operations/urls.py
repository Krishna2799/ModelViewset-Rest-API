from django.urls import URLPattern
from rest_framework.routers import DefaultRouter
from .views import OperationsViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('Operations', OperationsViewSet)

urlpatterns = [
    path('api/', include(router.urls))

]
