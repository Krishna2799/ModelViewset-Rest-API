from rest_framework.viewsets import ModelViewSet
from .models import Operations
from .serializer import OperationsSerializer


class OperationsViewSet(ModelViewSet):
    serializer_class = OperationsSerializer
    queryset = Operations.objects.all()
