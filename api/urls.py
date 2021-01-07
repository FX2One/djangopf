from django.urls import path
#from .views import article_list, article_detail
from .views import ArticleAPIView, ArticleDetails


#created news URLS for our article_list VIEW
urlpatterns = [
    #path('article/', article_list),
    #path('detail/<int:pk>', article_detail),
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:pk>', ArticleDetails.as_view())
]

