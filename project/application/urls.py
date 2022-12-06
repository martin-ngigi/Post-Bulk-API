from django.urls import path
from .views import BookList

urlpatterns =[
    path('add/', BookList.as_view(), name='books'),
]