from django.urls import path
from .views import BookList

from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
			

router = DefaultRouter()
router.register(r'add-multiple', BookViewSet, basename='user') #http://127.0.0.1:8000/books/add-multiple/
#urlpatterns = router.urls

urlpatterns =[
    path('add/', BookList.as_view(), name='books'), #http://127.0.0.1:8000/books/add/
] + router.urls