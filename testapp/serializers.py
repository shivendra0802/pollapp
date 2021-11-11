from django.db.models import fields
from rest_framework import serializers
from .models import NewModel, TestModel, Album, Track


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewModel
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='track-detail'
    )

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']    
