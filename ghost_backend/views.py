from rest_framework import viewsets
from ghost_backend.models import Post
from ghost_backend.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
