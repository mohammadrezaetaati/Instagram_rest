from django.urls import path

from .views import PostCrud,Home
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostCrud, basename='post')
router.register('home', Home, basename='home')

urlpatterns = [
    # path('',PostList.as_view(),name='post'),
    # path('edit/<int:pk>',PostChanged.as_view(),name='postedit'),
    # path('test',PostTest.as_view(),name='postedit'),
]
urlpatterns = router.urls
