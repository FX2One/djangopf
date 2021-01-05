from django.contrib import admin
from .models import Article


# Register your models here.

#register from models.py Article class and imported above
admin.site.register(Article)
