from rest_framework import serializers
from .models import *


class CoordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coords
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'

    def to_internal_value(self, data):
        email = data.get('email')
        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            return super().to_internal_value(data)
        return {'id': user.id, 'email': email}


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = '__all__'


class PerevalSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    images = ImagesSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()

    class Meta:
        model = PerevalAdded
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'status', 'level',
                  'coords', 'user', 'images']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        email = user_data.get('email')
        images_data = validated_data.pop('images')
        coords_data = validated_data.pop('coords')
        level_data = validated_data.pop('level')

        user, _ = Users.objects.update_or_create(email=email, defaults=user_data)

        images = Images.objects.create(**images_data)
        coords = Coords.objects.create(**coords_data)
        level = Level.objects.create(**level_data)

        pereval = PerevalAdded.objects.create(user=user, images=images, coords=coords, level=level, **validated_data)
        pereval.save()
        return pereval