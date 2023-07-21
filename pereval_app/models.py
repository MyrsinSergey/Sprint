from django.db import models
from django.core.validators import RegexValidator

get_image_path = 'media/'
phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,12}$',
        message="Phone number must be entered in the format: "
                                         "'+999999999'. Up to 12 digits allowed.")

class Users(models.Model):
    email = models.EmailField(max_length=30, unique=True, verbose_name='Электронная почта')
    fam = models.CharField(max_length=150, verbose_name='Фамилия')
    name = models.CharField(max_length=150, verbose_name='Имя')
    otc = models.CharField(max_length=150, verbose_name='Отчество')
    phone = models.CharField(validators=[phone_regex], max_length=14, blank=True, verbose_name='Телефон')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Coords(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    height = models.FloatField(verbose_name='Высота')

    class Meta:
        verbose_name = "Координаты"
        verbose_name_plural = "Координаты"

class Level(models.Model):
    winter = models.CharField(max_length=10, verbose_name='Зима', null=True)
    summer = models.CharField(max_length=10, verbose_name='Лето', null=True)
    autumn = models.CharField(max_length=10, verbose_name='Осень', null=True)
    spring = models.CharField(max_length=10, verbose_name='Весна', null=True)

    def __str__(self):
        return f'{self.winter} {self.summer} {self.autumn} {self.spring}'

    class Meta:
        verbose_name = "Уровень сложности"
        verbose_name_plural = "Уровни сложности"

class Images(models.Model):
    title_1 = models.CharField(max_length=255, blank=True, verbose_name='Название фото 1')
    image_1 = models.ImageField(max_length=255, upload_to=get_image_path, blank=True, verbose_name='Фотография 1')
    title_2 = models.CharField(max_length=255, blank=True, verbose_name='Название фото 2')
    image_2 = models.ImageField(max_length=255, upload_to=get_image_path, blank=True, verbose_name='Фотография 2')
    title_3 = models.CharField(max_length=255, blank=True, verbose_name='Название фото 3')
    image_3 = models.ImageField(max_length=255, upload_to=get_image_path, blank=True, verbose_name='Фотография 3')

    def __str__(self):
        return f'{self.title_1} {self.title_2} {self.title_3}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class PerevalAdded(models.Model):
    NEW = 'new'
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    STATUS_CHOICES = [
    ('new', 'новый'),
    ('pending',  'модератор взял в работу'),
    ('accepted', 'модерация прошла успешно'),
    ('rejected',  'модерация прошла, информация не принята'),
    ]

    beauty_title = models.CharField(max_length=255, verbose_name='Название препятствия')
    title = models.CharField(max_length=255, verbose_name='Название вершины')
    other_titles = models.CharField(max_length=255, verbose_name='Другое название')
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user')
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    images = models.ForeignKey(Images, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=NEW, verbose_name='Статус')
    connect = models.TextField(null=True, verbose_name='Соединяет')

    def __str__(self):
        return f'{self.beauty_title} {self.title} {self.other_titles} id: {self.pk}, title:{self.title}'

    class Meta:
        verbose_name = "Перевал"
        verbose_name_plural = "Перевалы"


