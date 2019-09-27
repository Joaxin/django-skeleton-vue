from rest_framework import generics
from ..models import Category,Message
from .serializers import CategorySerializer,MessageSerializer
from rest_framework import viewsets

# class CategoryListView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryDetailView(generics.RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class MessageListView(generics.ListAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

# class MessageDetailView(generics.RetrieveAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer