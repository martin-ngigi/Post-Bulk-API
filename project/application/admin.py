from django.contrib import admin

# Register your models here.

from .models import Books, User, Account

admin.site.register(Books)
admin.site.register(User)
admin.site.register(Account)
