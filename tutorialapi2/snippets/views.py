from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer

from django.contrib.auth.models import User
from rest_framework import permissions,renderers,viewsets
from snippets.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import action






'''@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
# DefaultRouter  class we're using also automatically creates the API root view for us, so we can now delete the api_root function from our views
'''

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)




class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

