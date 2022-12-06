from django.shortcuts import render
#from django_model_mixins import mixins
from .models import Books
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status, mixins, generics, viewsets



'''
Can creata a list of books and a single book as well ;-)
Also accepts dict {} for a single object and a list/array [] for multiple objects
'''
class BookViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
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
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    search_fields = ('name','author')

    def create(self, request, *args, **kwargs):
        """
        #checks if post request data is an array initializes serializer with many=True
        else executes default CreateModelMixin.create function 
        """
        is_many = isinstance(request.data, list)
        if not is_many:
            return super(BookViewSet, self).create(request, *args, **kwargs)
        else:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
			


# POSTING LIST/ARRAY i.e []
'''
Can only create a list of objects only.
'''
#   URL -> https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
class BookList(generics.ListCreateAPIView):
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
