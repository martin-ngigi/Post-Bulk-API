from django.urls import path
from .views import BookList

from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
			

router = DefaultRouter()
router.register(r'add-multiple', BookViewSet, basename='user')
#urlpatterns = router.urls

urlpatterns =[
    path('add/', BookList.as_view(), name='books'),
] + router.urls