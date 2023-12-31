from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'fam', 'name', 'otc', 'phone']

    def to_internal_value(self, data):
        email = data.get('email')
        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            return super().to_internal_value(data)
        return {'id': user.id, 'email': email}


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ['image_1', 'title_1', 'image_2', 'title_2', 'image_3', 'title_3']


class PerevalSerializer(WritableNestedModelSerializer):
    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer()

    class Meta:
        model = PerevalAdded
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords',
                  'level', 'images']


    def create(self, validated_data, **kwargs):
        user_data = validated_data.pop('user')
        email = user_data.get('email')
        images_data = validated_data.pop('images')
        coords_data = validated_data.pop('coords')
        level_data = validated_data.pop('level')

        user, _ = Users.objects.update_or_create(email=email, defaults=user_data)

        images = Images.objects.create(**images_data)
        coords = Coords.objects.create(**coords_data)
        level = Level.objects.create(**level_data)

        pereval = PerevalAdded.objects.create(**validated_data, user=user, coords=coords, level=level, images=images,
                                              status='new')

        return pereval


class DetailedPerevalSerializer(WritableNestedModelSerializer):
    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer()

    class Meta:
        model = PerevalAdded
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords',
                  'level', 'images', 'status']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user = instance.user
            for key, value in user_data.items():
                setattr(user, key, value)
            user.save()
        return super().update(instance, validated_data)