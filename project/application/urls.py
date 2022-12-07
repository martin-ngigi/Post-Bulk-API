from django.urls import path
from .views import BookList, UserDetail

from .views import BookList, BookViewSet, AccountsViewSet
from rest_framework.routers import DefaultRouter
			

router = DefaultRouter()
router.register(r'add-multiple', BookViewSet, basename='user') # http://127.0.0.1:8000/books/add-multiple/
router.register(r'add-accounts', AccountsViewSet, basename='accounts') # http://127.0.0.1:8000/books/add-accounts/
#urlpatterns = router.urls

urlpatterns =[
    path('add/', BookList.as_view(), name='books'), # http://127.0.0.1:8000/books/add/
    path('add-user/', UserDetail.as_view(), name='user'), # http://127.0.0.1:8000/books/add-user/
    #path('add-accounts/', AccountsViewSet.as_view(), name='accounts'), # http://127.0.0.1:8000/books/add-accounts/

] + router.urls