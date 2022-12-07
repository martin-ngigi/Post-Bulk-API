from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=40)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' '+ self.author 

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name+' '+self.last_name

    class Meta:
        ordering = ["-first_name"]

class Account(models.Model):
    user = models.ForeignKey(User,related_name='account',on_delete=models.CASCADE) 
    account_name = models.CharField(max_length=40)
    create_date = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    

    def __str__(self):
        return self.account_name

    class Meta:
        ordering = ["-create_date"]

