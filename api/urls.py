from django.urls import path
from .views import article_list, article_detail

#created news URLS for our article_list VIEW
urlpatterns = [
    path('article/', article_list),
    path('detail/<int:pk>', article_detail)
]
