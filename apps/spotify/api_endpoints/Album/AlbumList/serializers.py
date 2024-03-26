from rest_framework.serializers import ModelSerializer
from apps.spotify.models import Album


class ALbumListSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ("title", "author", "cover")
