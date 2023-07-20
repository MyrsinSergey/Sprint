from rest_framework import serializers
from .models import *


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'
        verbose_name = 'Координаты'


class LevelSerialize(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'
        verbose_name = 'Уровень сложности'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'fam', 'name', 'otc', 'phone')
        verbose_name = 'Пользователь'


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('data', 'title')
        verbose_name = 'Изображение'


class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = ('beauty_title', 'title', 'other_titles', 'add_time', 'status')
        verbose_name = 'Перевал'