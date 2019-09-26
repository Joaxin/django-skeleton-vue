from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from .views import MessageViewSet

app_name = 'lime'


router = routers.DefaultRouter()
router.register('lime', MessageViewSet)


urlpatterns = [
#     path('category/',
#          views.CategoryListView.as_view(),
#          name='Category_list'),
#     path('category/<pk>/',
#          views.CategoryDetailView.as_view(),
#          name='Category_detail'),
#     path('messages/',
#          views.MessageListView.as_view(),
#          name='Messages_list'),
#     path('messages/<pk>/',
#          views.MessageDetailView.as_view(),
#          name='Messages_detail'),
     path('', include(router.urls)),
     path('admin/', admin.site.urls),
]
