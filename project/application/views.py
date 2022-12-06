from django.shortcuts import render
#from django_model_mixins import mixins
from .models import Books
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status, mixins, generics


# POSTING LIST/ARRAY i.e []
#URL -> https://stackoverflow.com/questions/22881067/django-rest-framework-post-array-of-objects
#    -> https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
class BookList(generics.ListCreateAPIView):

    """
    ViewSet create and list books

    Usage single : POST
    {
        "name":"Killing Floor: A Jack Reacher Novel", 
        "author":"Lee Child"
    }

    Usage array : POST
    [{  
        "name":"Mr. Mercedes: A Novel (The Bill Hodges Trilogy)",
        "author":"Stephen King"
    },{
        "name":"Killing Floor: A Jack Reacher Novel", 
        "author":"Lee Child"
    }]
    """

    model = Books
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
