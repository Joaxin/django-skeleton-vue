from django.urls import path
from . import views

app_name = 'lime'
urlpatterns = [
    # post views
    path('add/', views.add_link, name='add_link'),
    path('hao/', views.show_links, name='show_links'),
]