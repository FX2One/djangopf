from django.urls import path, include
#from .views import article_list, article_detail
from .views import ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'article',ArticleViewSet, basename="Article View Set")

#created news URLS for our article_list VIEW
urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    #path('article/', article_list),
    #path('detail/<int:pk>', article_detail),
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:pk>', ArticleDetails.as_view()),
    path('generic/article/<int:id>',GenericAPIView.as_view()),
]

