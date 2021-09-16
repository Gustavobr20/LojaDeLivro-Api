from rest_framework import viewsets

from .models import Livro
from .serializers import LivrosSerializer


class LivrosViewSet(viewsets.ModelViewSet):
        serializer_class = LivrosSerializer
        queryset = Livro.objects.all()