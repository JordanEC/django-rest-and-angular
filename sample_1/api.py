from rest_framework import viewsets, routers
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny
from auth_sample_1.serializers import UserSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (permissions.IsAuthenticated,)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)
