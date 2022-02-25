from . import models
from . import book_ser

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (ListModelMixin,
                                   CreateModelMixin,
                                   DestroyModelMixin,
                                   UpdateModelMixin,
                                   RetrieveModelMixin
                                   )
# Create your views here.


class BookView(GenericViewSet, ListModelMixin, CreateModelMixin):

    queryset = models.Book.objects
    serializer_class = book_ser.BookSerializer
