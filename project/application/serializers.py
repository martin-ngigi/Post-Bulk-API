from .models import Books, User, Account
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

#NB:: One user can have many accounts ie one-to-many relationship..
#first create user, then add account ;-)
class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = '__all__'