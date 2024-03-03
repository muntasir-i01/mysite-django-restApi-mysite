from django.urls import include, path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet, GenericArticleViewSet, ModelArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('article', GenericArticleViewSet, basename='article')
router.register('article', ModelArticleViewSet, basename='article')


urlpatterns = [
    path('viewset/modelview/', include(router.urls)),

    path('viewset/generic/', include(router.urls)),

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    

    path('article/class/', ArticleAPIView.as_view()),
    path('article/class/<int:id>/', ArticleDetails.as_view()), 

    path('article/generic/', GenericAPIView.as_view()),
    path('article/generic/<int:id>/', GenericAPIView.as_view()),


    path('article/function/', article_list),
    path('article/function/<int:pk>/', article_detail),
    
]   