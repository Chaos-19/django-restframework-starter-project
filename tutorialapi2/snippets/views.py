from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions

from snippets.permissions import IsOwnerOrReadOnly




#Using generic class-based views
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



# Using generic class-based views
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]





class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

