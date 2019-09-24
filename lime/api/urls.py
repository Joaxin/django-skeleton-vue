from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'lime'


# router = routers.DefaultRouter()
# router.register('lime', views.LimeViewSet)


urlpatterns = [
    path('category/',
         views.CategoryListView.as_view(),
         name='Category_list'),
    path('category/<pk>/',
         views.CategoryDetailView.as_view(),
         name='Category_detail'),
    path('favorites/',
         views.BookmarkListView.as_view(),
         name='Bookmark_list'),
    path('favorites/<pk>/',
         views.BookmarkDetailView.as_view(),
         name='Bookmark_detail'),
#     path('', include(router.urls)),
]
