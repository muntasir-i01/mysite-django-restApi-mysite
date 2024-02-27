from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView


urlpatterns = [
    path('article/function/', article_list),
    path('article/class/', ArticleAPIView.as_view()),
    path('article/generic/', GenericAPIView.as_view()),
    path('details/function/<int:pk>/', article_detail),
    path('details/class/<int:id>/', ArticleDetails.as_view()), 
]   