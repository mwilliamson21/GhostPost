from rest_framework.serializers import HyperlinkedModelSerializer
from ghost_backend.models import Post


class PostSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = [
            'is_boast',
            'post_content',
            'up_votes',
            'down_votes',
            'total_votes',
            'post_date'
        ]
